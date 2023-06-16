import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Ruta al archivo de configuración JSON generado en Firebase
cred = credentials.Certificate("tfg-data-173bc-firebase-adminsdk-9ixg4-59eb87bd6d.json")

# Inicializar la aplicación de Firebase
firebase_admin.initialize_app(cred)

# Obtener una instancia de Firestore
db = firestore.client()

# Referencia a la colección y el documento específico
coleccion = db.collection('tfg')
ultimos_documentos = coleccion.order_by('time_stamp', direction=firestore.Query.DESCENDING).limit(5).get()

# Obtener los datos del documento
for documento in ultimos_documentos:
    datos = documento.to_dict()

    # Guardar los datos en un archivo JSON
    print(datos['time_stamp'].replace(" ","-"))
    with open('documento'+str(datos['time_stamp'].replace(" ","-").replace(":","-"))+'.json', 'w') as archivo_json:
        json.dump(datos, archivo_json,indent=4)

# Finalizar la aplicación de Firebase
firebase_admin.delete_app(firebase_admin.get_app())
