## Aufgabe 1
    Mit Hilfe der Module multiprocessing, threading und asyncio der Python-Standardbibliothek können nebenläufige Aufgaben auf unterschiedliche Weise realisiert werden. Beschreiben Sie für jedes der drei Module kurz, ob die Nebenläufigkeit durch Prozesse, Threads oder Co-Routinen erfolgt und welche Art der Parallelausführung sie deshalb unterstützen. Nennen Sie zusätzlich jeweils einen typischen Anwendungsfall.
### Module multiprocessing:
    Die Nebenläufigkeit erfolgt durch Prozesse. Die parallele Ausführung unterstützt somit die Parallelverarbeitung auf mehreren Kernen. Ein typischer Anwendungsfall ist die Beschleunigung von aufwendigen Berechnungen auf Multi-Core-Systemen.

### Module threading:
    Die Nebenläufigkeit erfolgt durch Threads. Die parallele Ausführung unterstützt somit die Nebenläufigkeit innerhalb eines einzelnen Prozesses. Ein typischer Anwendungsfall ist die gleichzeitige Ausführung von mehreren Aufgaben, die jedoch nicht auf mehrere Prozessoren verteilt werden müssen.

### Module asyncio:
    Die Nebenläufigkeit erfolgt durch Co-Routinen. Die parallele Ausführung unterstützt somit die Verarbeitung von vielen gleichzeitigen Anfragen in einem einzigen Thread. Ein typischer Anwendungsfall ist die Verarbeitung von Netzwerk- oder I/O-Anfragen, bei denen es viele kleine Anfragen gibt, die jedoch schnell bearbeitet werden müssen.