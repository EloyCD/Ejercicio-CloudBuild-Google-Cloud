import json
from google.cloud import storage
from google.cloud import firestore

storage_client = storage.Client()
firestore_client = firestore.Client()

def read_json_from_gcs(event, context):
    # Verifica si el evento proviene de Cloud Storage


        # Descarga el archivo desde Cloud Storage
        blob = storage_client.bucket(event["bucket"]).get_blob(event["name"])
        content = blob.download_as_text()

        # Lee y muestra el contenido del archivo JSON
        data = json.loads(content)
        
        print(data)
        firestore_client.collection("mibasedeporlatarde").add(data)
