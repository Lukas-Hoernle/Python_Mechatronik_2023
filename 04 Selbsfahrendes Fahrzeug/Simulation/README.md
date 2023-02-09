Carbot: Device Firmware
-----------------------

Dies ist eine vereinfachte Variante des „Carbot” selbstfahrenden Fahrzeugs
zur Simulation auf dem eigenen Laptop. Es werden kein Rasbperry Pi und keine
Hardwarebausteine benötigt, da die Hardware komplett mit [tkgpio](https://github.com/wallysalami/tkgpio)
simuliert wird.

![Foto](screenshot.png)

Analog der großen Vorlage ist die  Hardwarekonfiguration ist vollständig in der
Datei `carbot/main.py` gekapselt, so dass die Programmierung leicht angepasst werden
kann. Ebenso ist der Quellcode weitgehend modular aufgebaut. Im Gegensatz zur
großen Lösung werden hier jedoch asynchrone Coroutinen mit der `async/await`-Syntax
verwendet, um die nebenläufigen Prozesse mit den Fahrzeugfunktionen zu implementieren.
Die Prozesse selbst sind aber dieselben:

 * Der `DistanceSensor` liest das Attribute `direction` aus, um den Servomotor zur
   Ausrichtung des Abstandsmessers zu positionieren.

 * Der `ObstacleSensor` erkennt Hindernisse vor dem Fahrzeug und ändert den
   Parameter `obstacle_pushback` mit abnehmender Entfernung, um das Fahrzeug
   zu verlangsamen.

 * …

Die Klassen `LineSensor` und `ManualDrive` sind hingegen nur als Stub angelegt und
müssen von den Studierenden aus Übung selbst implementiert werden.