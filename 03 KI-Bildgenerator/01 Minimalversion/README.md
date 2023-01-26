I-Paint: Minimalversion
-----------------------

Dies ist die simpelste Version des Beispiels. Es handelt sich um ein ganz
einfaches Python-Skript, das immer dieselbe Anfrage an die DALL-E API sendet
und dann ein Browserfenster mit dem Ergebnis öffnet.

Die Abhängigkeiten für diese Version wurden mit folgenden Befehlen installiert:

 * `poetry add openai`
 * `poetry add pysnooper --group dev`
 * `poetry add pudb --group dev`

Wobei die letzten beiden nur Helfer zum Debuggen sind und deshalb auch nur als
Entwicklungabhängigkeiten installiert wurden.

Rufen Sie `poetry install` in diesem Verzeichnis auf, um ein Python Environment
mit diesen Bibliotheken auf dem eigenen Rechner anzulegen.