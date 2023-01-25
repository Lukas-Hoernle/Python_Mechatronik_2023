KI-Bildgenerator
================

Dieses Beispiel nutzt die öffentliche API des DALL-E Bildgenerators von OpenAI.

 * DALL-E Weboberfläche: https://labs.openai.com/
 * API-Beschreibung: https://beta.openai.com/docs/guides/images
 * Tutorial auf Realpython.com: https://realpython.com/generate-images-with-dalle-openai-api/

Auf folgender Seite muss zunächst ein API-Key erzeugt werden:
https://beta.openai.com/account/api-keys

In diesem Verzeichnis muss dann eine Textdatei namens API_KEY.json angelegt werden,
in welcher der Key hineinkopiert werden muss. Die Datei wird nicht mit Git
versioniert und findet sich deshalb auch nicht auf GitHub. Der Inhalt muss wie
folgt aussehen:

  ```json
  {
    "organization": "ID DER EIGENEN ORGANISATION",
    "api_key": "EIGENER API KEY"
  }
  ```

 * API-Key generieren: https://beta.openai.com/account/api-keys
 * Seite mit der Organisation-ID: https://beta.openai.com/account/org-settings
 * Verbleibendes Guthaben: https://beta.openai.com/account/usage