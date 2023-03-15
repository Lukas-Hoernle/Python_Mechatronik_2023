import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainWindow:
    """
    Hauptfenster der Anwendung.
    """

    def __init__(self, connection):
        """
        Konstruktor. Hier werden die tkinter-Widgets erstellt. Als Parameter muss ein zuvor
        erzeugte Instanz der Klasse RemoteConnection übergeben werden.
        """
        # Das Fenster selbst
        self._root = ttk.Window(title="Carbot Fernsteuerung", size=(1200, 600), resizable=(False, False))
        self._root.columnconfigure(1, weight=1)
        self._root.place_window_center()

        # Verbindung zum Fahrzeug
        connection_frame = self._create_row_frame(self._root, row=0, text="IP-Adresse", dark=True)
        
        self._remote_ip = tk.StringVar(value="192.168.178.121")
        self._connect_button_text = tk.StringVar(value="Verbindung herstellen")
        self._connected = False

        self._remote_ip_entry = ttk.Entry(connection_frame, width=20, textvariable=self._remote_ip)
        self._remote_ip_entry.grid(row=0, column=1, sticky=(N,E,S,W))

        self._connect_button = ttk.Button(connection_frame, textvariable=self._connect_button_text, bootstyle=PRIMARY, command=self._on_toggle_connection)
        self._connect_button.grid(row=0, column=2, sticky=(W))

        self._update_connection_widgets()

        # Sensoren
        self._sensor_frame = self._create_row_frame(self._root, row=1, text="Sensorstatus")
        self._sensor_widgets = {}
        self._sensor_status  = {}

        self._update_sensor_widgets()

        # Audiowiedergabe
        self._sound_frame = self._create_row_frame(self._root, row=2, text="Audiowiedergabe")
        self._sound_widgets = {}
        self._sound_status  = {}

        self._update_sound_widgets()
        
        # Fahrzeugparameter        
        vehicle_frame = self._create_row_frame(self._root, row=3, text="Fahrzeugparameter")
        self._vehicle_status = {}

        self._update_vehicle_widgets()

        # Dummy zum Ausfüllen des Fensters nach unten
        self._root.rowconfigure(4, weight=1)
        self._create_row_frame(self._root, row=4)

        # Rückruffunktionen für die Klasse RemoteConnection registrieren
        self._connection = connection

        connection.on_connection_change      = self._on_connection_change
        connection.on_receive_vehicle_status = self._on_receive_vehicle_status
        connection.on_receive_sensor_status  = self._on_receive_sensor_status
        connection.on_receive_sound_status   = self._on_receive_sound_status
    
    def _create_row_frame(self, root, row, text="", dark=False):
        """
        Hilfsmethode zum Erzeugen eines Labels und Frames mit einer visuellen Zeile
        im Hauptfenster. Das Laben befindet sich am linken Rand und hat einen dunklen
        Hintergrund. Der eigentliche Inhalt befindet sich rechts davon in einem Frame
        mit maximaler Breite und hellem Hintergrund.

        Parameter:
          * root: Elternelement
          * row: Zeile innerhalb des Elternelements, beginnend bei 0
          * text: Bezeichnung am linken Rand
          * dark: Flag für dunkleren Hintergrund
        
        Rückgabe: Frame für den eigentlichen Inhalt
        """
        ttk.Label(root, text=text, bootstyle=(INVERSE, DARK), padding=(6,6,24,6)).grid(row=row, column=0, sticky=(N,E,S,W))

        frame = ttk.Frame(root, bootstyle=SECONDARY if dark else LIGHT, padding=6)
        frame.grid(row=row, column=1, sticky=(N,E,S,W))
        frame.columnconfigure(0, weight=1)

        return frame

    # -----------------------
    # Verbindung zum Fahrzeug
    # -----------------------
    def _on_toggle_connection(self):
        """
        Klick auf den Button zum Herstellen oder Trennen der Verbindung.
        """
        if not self._connected:
            remote_ip = self._remote_ip.get()
            self._connection.connect(remote_ip)
        else:
            self._connection.disconnect()

    def _on_connection_change(self, connected):
        """
        Vom Netzwerk-Thread aufgerufene Rückruffunktion zur Aktualisierung des UIs nach
        einer Änderung des Verbindungsstatus.
        """
        def _in_ui_thread():
            self._connected = connected
            self._update_connection_widgets()

        self._root.after_idle(_in_ui_thread)

    def _update_connection_widgets(self):
        """
        Widgets zur Verbindung mit dem Fahrzeug aktualisieren.
        """
        if self._connected:
            self._remote_ip_entry.configure(state=DISABLED)

            self._connect_button_text.set("Verbindung trennen")
            self._connect_button.configure(bootstyle=DANGER)
        else:
            self._remote_ip_entry.configure(state="")

            self._connect_button_text.set("Verbindung herstellen")
            self._connect_button.configure(bootstyle=PRIMARY)

    # --------
    # Sensoren
    # --------
    def _on_receive_sensor_status(self, sensor_status):
        """
        Vom Netzwerk-Thread aufgerufene Rückruffunktion zur Aktualisierung des UIs nach
        dem Empfang neuer Sensorinformationen.
        """
        def _in_ui_thread():
            self._sensor_status = sensor_status
            self._update_sensor_widgets()

        self._root.after_idle(_in_ui_thread)

    def _update_sensor_widgets(self):
        """
        Widgets für den Sensorstatus aktualisieren.
        """
        pass

    # ---------------
    # Audiowiedergabe
    # ---------------
    def _on_receive_sound_status(self, sound_status):
        """
        Vom Netzwerk-Thread aufgerufene Rückruffunktion zur Aktualisierung des UIs nach
        dem Empfang neuer Statusinformationen des Audioplayers.
        """
        def _in_ui_thread():
            self._sound_status = sound_status
            self._update_sound_widgets()

        self._root.after_idle(_in_ui_thread)

    def _update_sound_widgets(self):
        """
        Widgets für die Audiowiedergabe aktualisieren.
        """
        pass

    # -----------------
    # Fahrzeugparameter
    # -----------------
    def _on_receive_vehicle_status(self, vehicle_status):
        """
        Vom Netzwerk-Thread aufgerufene Rückruffunktion zur Aktualisierung des UIs nach
        dem Empfang neuer Fahrzeugparameter.
        """
        def _in_ui_thread():
            self._vehicle_status = vehicle_status
            self._update_vehicle_widgets()

        self._root.after_idle(_in_ui_thread)

    def _update_vehicle_widgets(self):
        """
        Widgets für die Fahrzeugdaten aktualisieren.
        """
        pass

    # --------------------
    # Öffentliche Methoden
    # --------------------
    def mainloop(self):
        """
        Blockierende Methode zur Ausführung der tkinter "Hauptschleife". Diese Methode
        muss nach Erzeugung des Objekts aufgerufen werden, damit die Anwendung auf
        Ereignisse reagieren kann. Die Methode wird erst beendet, wenn das Programm
        beendet werden soll.
        """
        self._root.mainloop()