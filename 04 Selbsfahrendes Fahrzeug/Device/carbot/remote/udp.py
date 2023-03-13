import collections, errno, json, socket, threading, time, traceback
from carbot.sensors.base import SensorBase

# https://docs.python.org/3/library/socketserver.html#asynchronous-mixins
# https://wiki.python.org/moin/UdpCommunication
# https://pythontic.com/modules/socket/udp-client-server-example

# https://docs.python.org/3/library/collections.html#collections.deque
# https://docs.python.org/3/library/threading.html#lock-objects
# https://docs.python.org/3/library/json.html#module-json

class UDPRemoteControl(SensorBase):
    """
    Fernsteuerung des Fahrzeugs durch entfernte UDP-Clients. Startet einen Hintergrundthread,
    in dem ein UDP-Socket zum Empfangen von Steuerbefehlen geöffnet wird. Folgende Befehle
    werden dabei unterstützt:

        * Abruf der Fahrzeugparameter
        * Geschwindigkeit ändern
        * Richtung ändern
        * Vorhandene Sensoren abfragen
        * Sensor aktivieren/deaktivieren
        * Soundfile abspielen/stoppen
    
    Die Kommandos werden als UTF-8 kodiertes JSON-Objekt der Form `{"cmd": "...", ...}`
    übertragen, wobei auf die meisten Kommandos keine Antwort erfolgt.

    Kommandos ohne direkte Antwort:

        * `{"cmd": "set", "attr": "target_speed", "value": 0}`
        * `{"cmd": "set", "attr": "direction", "value": 0}`
        * `{"cmd": "enable_sensor", "name": "…"}`
        * `{"cmd": "disable_sensor", "name": "…"}`
        * `{"cmd": "soundplayer", "action": "play", "soundfile": "…"}`
        * `{"cmd": "soundplayer", "action": "stop", "soundfile": "…"}`
    
    Kommandos mit direkter Antwort:

        * `{"cmd": "vehicle_status"}`
          liefert als Antwort ein Objekt mit den Fahrzeugparametern und ihren Werten.

        * `{"cmd": "sensor_status"}`
          liefert als Antwort ein Objekt mit den Sensornamen und einem Aktiv-Flag.
        
        * `{"cmd": "soundplayer", "action": "get_soundfiles"}`
          liefert als Antwort eine Liste mit den Namen der verfügbaren Sounds.

        * `{"cmd": "soundplayer", "action": "get_playing"}`
          liefert als Antwort eine Liste mit den Namen der gerade wiedergegebenen Sounds.
    
    Die Nachrichten in beide Richtungen dürfen nicht größer als 4096 Bytes sein.
    """

    _BUFFER_SIZE = 4096
    _TIMEOUT_S = 0.1

    def __init__(self, host, port):
        """
        Konstruktor. Startet einen Server-Thread und öffnet darin einen UDP-Socket für die
        Abwicklung des entfernten Datenaustauschs.

        Parameter:
            * host: Hostname, an den der UDP-Socket gebunden wird
            * port: Portnummer, an den der UDP-Socket gebunden wird
        
        Wird für `host` ein leerer String übergeben, lauscht der Server auf allen Adressen und
        allen Netzwerkschnittstellen, wodurch er von entfernten Clients angesprochen werden kann.
        Wird stattdessen der Wert "localhost" oder eine IP-Adresse übergeben, kann der Server nur
        aus dem dazugehörigen IP-Netz (bei "localhost" also nur von der eigenen Maschine) erreicht
        werden.
        """
        super().__init__()

        self._host = host or None
        self._port = port

        self._pending_commands = collections.deque()
        self._vehicle_status   = {}
        self._sensor_status    = {}
        self._sound_player     = None
        self._available_sounds = []
        self._playing_sounds   = []
        self._status_lock      = threading.Lock()
        self._server_thread    = threading.Thread(target=self._server_thread_loop)

        self._server_thread.setDaemon(True)
        self._server_thread.start()
    
    def _server_thread_loop(self):
        """
        Hauptschleife des Server-Threads. Öffnet den UDP-Socket und bearbeitet die darüber empfangenen
        Kommandos. Anfragen nach dem Fahrzeugstatus werden anhand der letzten internen Kopie des
        Fahrzeugstatus direkt beantwortet. Alle anderen Anfragen werden in einer FIFO-Queue gesammelt
        und vom Fahrzeug-Thread bei nächster Gelegenheit abgearbeitet.
        """
        # Sockets öffnen sowohl für UPv6 als auch IPv4
        sockets = []

        for address_info in socket.getaddrinfo(self._host, self._port, proto=socket.IPPROTO_UDP):
            try:
                socket_ = socket.socket(
                    family = address_info.af,
                    type   = address_info.socktype | socket.SOCK_NONBLOCK,
                    proto  = address_info.proto
                )

                socket_.bind((self._host, self._port))
                sockets.append(socket_)
            except:
                pass
        
        # UDP-Pakete über die Sockets empfangen und verarbeiten
        sockets_without_data = 0

        while True:
            if sockets_without_data == len(sockets):
                # Kleine Pause zur Entlastung der CPU, wenn kein Socket Daten liefert
                time.sleep(self._TIMEOUT_S)

            sockets_without_data = 0

            for socket_ in sockets:
                try:
                    # Neue Daten vom Socket empfangen und verarbeiten
                    data, address = socket_.recvfrom(self._BUFFER_SIZE)
                    command = json.loads(data)

                    if not hasattr(command, "cmd"):
                        continue

                    if command.cmd == "vehicle_status":
                        # Abfrage des Fahrzeugstatus direkt beantworten
                        with self._status_lock:
                            response = json.dumps(self._vehicle_status)
                            socket_.sendto(response, address)
                    elif command.cmd == "sensor_status":
                        # Abfrage des Sensorstatus direkt beantworten
                        with self._status_lock:
                            response = json.dumps(self._sensor_status)
                            socket_.sendto(response, address)
                    elif command.cmd == "soundplayer" and command.action == "get_soundfiles":
                        with self._status_lock:
                            response = json.dumps(self._available_sounds)
                            socket_.sendto(response, address)
                    elif command.cmd == "soundplayer" and command.action == "get_playing":
                        with self._status_lock:
                            response = json.dumps(self._playing_sounds)
                            socket_.sendto(response, address)
                    else:
                        # Alle anderen Steuerbefehle im Fahrzeug-Thread bearbeiten
                        self._pending_commands.append(command)
                except OSError as err:
                    if err.errno == errno.EAGAIN or err.errno == errno.EWOULDBLOCK:
                        sockets_without_data += 1
                        continue
                    else:
                        print(f"Socket-Fehler: {err}")
                        traceback.print_exc()
                except Exception as exc:
                    print(f"Fehler im Server-Thread: {exc}")
                    traceback.print_exc()

    def update(self, vehicle):
        """
        Im Fahrzeug-Thread regelmäßig aufgerufene Methode, in der der aktuelle Fahrzeugstatus ermittelt
        sowie das Fahrzeug gesteuert werden kann. Der aktuelle Fahrzeugstatus wird als internes Objekt
        zwischengespeichert, um Anfragen nach dem Status direkt im Server-Thread bearbeiten zu können.
        Anschließend werden die vom Server-Thread zwischenzeitlich gesammelten Steuerbefehle abgearbeitet.
        """
        # Aktuellen Fahrzeugstatus merken
        if self._status_lock.acquire(blocking=False):
            # Fahrzeugstatus ermitteln
            self._vehicle_status = {
                "line_pattern":      vehicle.line_pattern,
                "target_speed":      vehicle.target_speed,
                "obstacle_pushback": vehicle.obstacle_pushback,
                "direction":         vehicle.direction,
                "speed_total":       vehicle.speed_total,
                "speed_left":        vehicle.speed_left,
                "speed_right":       vehicle.speed_right,
            }

            self._sensor_status = vehicle.sensor_status.copy()
        
            # Soundplayer-Objekt merken und ggf. verfügbare Sounds einlesen, wenn der Player aktiviert wird
            if not self._sound_player:
                try:
                    sound_player = vehicle.get_sensor("sound:player")
                except KeyError:
                    sound_player = None

                if sound_player and sound_player.is_active:
                    self._sound_player     = sound_player
                    self._available_sounds = self._sound_player.soundfiles
                    self._playing_sounds   = self._sound_player.playing
            else:
                if self._sound_player.is_active:
                    self._playing_sounds = self._sound_player.playing
                else:
                    self._sound_player     = None
                    self._available_sounds = []
                    self._playing_sounds   = []

            # Sperre aufheben
            self._status_lock.release()
        
        # Empfangene Steuerbefehle verarbeiten
        while True:
            try:
                command = self._pending_commands.pop()
            except IndexError:
                break

            command_ = {
                "cmd": getattr(command, "cmd", ""),
                "attr": getattr(command, "attr", ""),
                "value": getattr(command, "value", ""),
                "name": getattr(command, "name", ""),
            }
            
            if command_.cmd == "set" and command_.attr == "target_speed":
                # Zielgeschwindigkeit ändern
                try:
                    vehicle.target_speed = int(command_.value)
                except ValueError:
                    pass
            elif command_.cmd == "set" and command_.attr == "direction":
                # Fahrtrichtung ändern
                try:
                    vehicle.direction = int(command_.value)
                except ValueError:
                    pass
            elif command_.cmd == "enable_sensor":
                # Sensor aktivieren
                try:
                    sensor = vehicle.get_sensor(command_.name)
                    sensor.enable()
                except:
                    pass
            elif command_.cmd == "disable_sensor":
                # Sensor deaktivieren
                try:
                    sensor = vehicle.get_sensor(command_.name)
                    sensor.disable()
                except:
                    pass
            elif command_.cmd == "soundplayer" and command_.action == "play":
                if self._sound_player:
                    self._sound_player.play(command_.soundfile)
            elif command_.cmd == "soundplayer" and command_.action == "stop":
                if self._sound_player:
                    self._sound_player.stop(command_.soundfile)
