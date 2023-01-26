I-Paint: Der KI-Bildgenerator
=============================

Dieses Beispiel nutzt die öffentliche API des DALL-E Bildgenerators von OpenAI.

 * DALL-E Weboberfläche: https://labs.openai.com/
 * API-Beschreibung: https://beta.openai.com/docs/guides/images
 * Tutorial auf Realpython.com: https://realpython.com/generate-images-with-dalle-openai-api/

Varianten des Beispiels
-----------------------

 * *****01 Minimalversion:** Super einfaches Python-Skript zum Aufruf der API
 * **02 Klassenbasierte Struktur:** Erste Zwischenversion auf dem Weg zu einer richtigen Anwendung
 * **03 Grafische Oberfläche:** Noch bessere Version, die zusätzlich ein Text UI besitzt

Die verschiedenen Versionen bauen aufeinander auf, wobei die erste Version nur
ein paar einfache Sprachfeatures von Python demonstrieren soll. Ab der zweiten
Version beginnt dann die *Überarbeitung zu einer richtigen Anwendung, die hierfür
sinnvoll in Klassen und Module gegliedert wurde. Die dritte Version baut darauf
auf und ersetzt das bis dahin sehr minimalistisch User Interface durch ein modernes
Text User Interface (eine Art GUI im Terminalfenster).

Vorbereitung
------------

Auf folgender Seite muss zunächst ein API-Key erzeugt werden:
https://beta.openai.com/account/api-keys

In diesem Verzeichnis muss dann eine Textdatei namens API_KEY.json angelegt werden,
in welcher der Key hineinkopiert werden muss. Die Datei wird nicht mit Git
versioniert und findet sich deshalb auch nicht auf GitHub. Der Inhalt muss wie
folgt aussehen:

  ```json
  {
    "openai": {
      "organization": "ID DER EIGENEN ORGANISATION",
      "api_key": "EIGENER API KEY"
    }
  }
  ```

 * API-Key generieren: https://beta.openai.com/account/api-keys
 * Seite mit der Organisation-ID: https://beta.openai.com/account/org-settings
 * Verbleibendes Guthaben: https://beta.openai.com/account/usage

Ausführen der Beispiele
-----------------------

Die Beispiele verwenden jeweils [Peotry](https://python-poetry.org) zur
Verwaltung der Abhängigkeiten und des Python Environments. Die Beispiele
können im jeweiligen Unterverzeichnis mit `peotry run python ipaint/main.py`
ausgeführt werden.

Weitere Einzelheiten zu Poetry finden sich im Beispielquellcode zur
Anlage neuer Python-Projekte.
