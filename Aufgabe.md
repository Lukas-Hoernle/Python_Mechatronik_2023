## Aufgabe 1 a)
Mit Hilfe der Module multiprocessing, threading und asyncio der Python-Standardbibliothek können nebenläufige Aufgaben auf unterschiedliche Weise realisiert werden. Beschreiben Sie für jedes der drei Module kurz, ob die Nebenläufigkeit durch Prozesse, Threads oder Co-Routinen erfolgt und welche Art der Parallelausführung sie deshalb unterstützen. Nennen Sie zusätzlich jeweils einen typischen Anwendungsfall.
### Module multiprocessing:
Die Nebenläufigkeit erfolgt durch Prozesse. Die parallele Ausführung unterstützt somit die Parallelverarbeitung auf mehreren Kernen. Ein typischer Anwendungsfall ist die Beschleunigung von aufwendigen Berechnungen auf Multi-Core-Systemen.

### Module threading:
Die Nebenläufigkeit erfolgt durch Threads. Die parallele Ausführung unterstützt somit die Nebenläufigkeit innerhalb eines einzelnen Prozesses. Ein typischer Anwendungsfall ist die gleichzeitige Ausführung von mehreren Aufgaben, die jedoch nicht auf mehrere Prozessoren verteilt werden müssen.

### Module asyncio:
Die Nebenläufigkeit erfolgt durch Co-Routinen. Die parallele Ausführung unterstützt somit die Verarbeitung von vielen gleichzeitigen Anfragen in einem einzigen Thread. Ein typischer Anwendungsfall ist die Verarbeitung von Netzwerk- oder I/O-Anfragen, bei denen es viele kleine Anfragen gibt, die jedoch schnell bearbeitet werden müssen.
## Aufgabe 1 b)
Die interne Steuerung eines IoT-Devices wurde mit Co-Routinen programmiert. Innerhalb einer Co-Routine kommt es jedoch immer mal wieder vor, dass die Methode zum Auslesen eines Sensors drei Sekunden benötigt, um den Sensorwert zu ermitteln. Welches Problem ergibt sich daraus, wenn es sich bei der Methode um eine so genannte „blockierende Methode“ handelt und wie könnte es gelöst werden?
### Erklärung 
Wenn eine blockierende Methode in einer Co-Routine aufgerufen wird, kann dies dazu führen, dass die gesamte Co-Routine für die Dauer der Ausführung der Methode blockiert wird und keine anderen Aufgaben ausgeführt werden können. Dies kann zu einer ineffizienten Nutzung der Ressourcen und Verzögerungen in anderen Prozessen führen.

### Lösung
Um dieses Problem zu lösen, können wir asynchrone Methoden verwenden, die das Auslesen des Sensors in einem separaten Thread oder Prozess ausführen, um sicherzustellen, dass die Co-Routine nicht blockiert wird. Alternativ können wir auch asynchrone I/O-Operationen verwenden, um den Sensorwert zu ermitteln, indem wir den Aufruf der blockierenden Methode in eine asynchrone Funktion einbetten und sie mit der await-Anweisung aufrufen. Dadurch wird die Co-Routine nicht blockiert, sondern kehrt zurück, während die I/O-Operation im Hintergrund ausgeführt wird.

## Aufgabe 2 a)
```
   +-------------+
   | Button Task |--------------+----------------------+
   +-------------+              |                      |
         |                      |                      |
         V                      |                      V
   +-------------+              |               +-------------+
   | Blinker Task|              |               |    Hupe     |
   +-------------+              |               +-------------+
         |                      |
         V                      V
  +--------------+      +--------------+
  | Licht Task   |      | Wischer Task |
  +--------------+      +--------------+
```
* Task "Button": Wartet auf Button-Events und ändert den Hupe-Status, den Blinkerstatus oder den Wischerstatus (je nachdem welcher Button gedrückt wurde) entsprechend. Der Task läuft in 3 Instanzen und achtet je auf eine Hardware. Hier vereinfacht dargestellt.
* Task "Blinker": Schaltet die Blinker anhand der aktuellen Einstellung (Links, Rechts, Warnblinker) ein oder aus.
* Task "Licht": Schaltet das Fahrtlicht anhand der aktuellen Einstellung (Abblendlicht, Fernlicht, Lichtsensor) ein oder aus.
* Task "Wischer": Schaltet den Scheibenwischer anhand der aktuellen Einstellung (Intervallwischen langsam, Intervallwischen schnell, Regensensor) ein oder aus.
## Aufgabe 2 b) 
Legen Sie ein neues Python-Projekt an oder kopieren Sie den Quellcode aus der Vorlesung und entfernen dabei alle Quellcodes, die für diese Aufgabe nicht benötigt werden. Das neue Projekt sollte zunächst nur ei - ne Datei requirements.txt zur Installation der Bibliotheken, ein Startskript, ein Hauptmodul sowie eine JSON-Datei zur Beschreibung der Hardwarebausteine beinhalten.