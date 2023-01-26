I-Paint: Grafische Oberfläche
-----------------------------

Diese Version baut auf der vorherigen Version auf und ersetzt die bisher sehr
spärliche Benutzerinteraktion durch ein modernes Text User Interface. Der
meiste Quellcode ist daher identisch. Lediglich die `main.py` musste hierfür
neugeschrieben werden.

Die Abhängigkeiten für diese Version wurden mit folgenden Befehlen installiert:

 * `poetry add openai`
 * `poetry add textual`
 * `poetry add pysnooper --group dev`
 * `poetry add pudb --group dev`

Wobei die letzten beiden nur Helfer zum Debuggen sind und deshalb auch nur als
Entwicklungabhängigkeiten installiert wurden.

Rufen Sie `poetry install` in diesem Verzeichnis auf, um ein Python Environment
mit diesen Bibliotheken auf dem eigenen Rechner anzulegen.