I-Paint: Klassenbasierte Struktur
---------------------------------

Diese Version unterscheidet sich deutlich von der Vorgängerversion. Das simple
Skript hat sich zu einer richtigen kleinen Anwendung gemausert, die sich aus
mehreren Klassen und Modulen zusammensetzt.

So gibt es nun eine `ApiKeyManager` genannte Klasse zum Einlesen der API Keys und
ein Unterpaket mit den Namen `Generator`, dass eine allgemeine Schnittstelle für
Text2Image-Bildgeneratoren sowie eine konkrete Implementierung dieser für OpenAI
DALL-E beinhaltet. Aufgabe des Hauptprogramms ist es daher nun, die Interaktion
mit dem Anwender abzubilden (den Anwender zu fragen, was er will) und hierbei
die richtigen Klassen zu verwenden.

Auf dieser Grundlage kann das Programm nun beliebig weiterentwickelt werden:

 1. Integration weiterer Text2Image APIs (z.B. auf huggingface.io)
 2. Implementierung einer nicht-interaktiven Kommandozeilenversion
 3. Implementierung einer grafischen Benutzeroberfläche
 4. Implementierung einer eigenen Webservice API
 5. Und so weiter. Der Fantasie sind keine Grenzen gesetzt. :-)

Die Abhängigkeiten für diese Version wurden mit folgenden Befehlen installiert:

 * `poetry add openai`
 * `poetry add pysnooper --group dev`
 * `poetry add pudb --group dev`

Wobei die letzten beiden nur Helfer zum Debuggen sind und deshalb auch nur als
Entwicklungabhängigkeiten installiert wurden.

Rufen Sie `poetry install` in diesem Verzeichnis auf, um ein Python Environment
mit diesen Bibliotheken auf dem eigenen Rechner anzulegen.