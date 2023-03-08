import os
import sys
import time
import json
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Constantes
FOLDER_PATH2 = "data_firebase/"
FOLDER_PATH=""
WAIT_TIME = 3 # Tiempo de espera para la conexión a internet en segundos

# Funciones
def is_connected():
    """
    Comprueba si hay conexión a internet.
    """
    try:
        requests.get("http://www.google.com")
        return True
    except:
        return False

def save_local_data(filename, data):
    """
    Guarda los datos localmente.
    """
    if not os.path.exists(FOLDER_PATH2):
        os.makedirs(FOLDER_PATH2)
    with open(os.path.join(FOLDER_PATH2, filename), "w") as f:
        json.dump(data, f)

def sync_local_data():
    """
    Sincroniza los datos guardados localmente con Firestore.
    """
    if not os.path.exists(FOLDER_PATH):
        return
    for filename in os.listdir(FOLDER_PATH):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(FOLDER_PATH, filename)) as f:
            data = json.load(f)
        doc_name = 'data_' + str(sys.argv[1])
        db.collection('tfg').document(doc_name).set(data)
        os.remove(os.path.join(FOLDER_PATH, filename))

# Comprobar si hay datos guardados localmente y sincronizarlos con Firestore
sync_local_data()

# Comprobar si se ingresó un nombre de archivo
if len(sys.argv) < 2:
    print('Error: Debe ingresar el nombre del archivo JSON como argumento.')
    sys.exit()

# Inicializar Firebase
cred = credentials.Certificate("tfg-data-173bc-firebase-adminsdk-9ixg4-59eb87bd6d.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://tfg.firebaseio.com/'})
db = firestore.client()

# Leer el archivo JSON especificado
filename = sys.argv[1]
filename="ST_data.json"
with open(filename) as f:
    data = json.load(f)

# Esperar a que haya conexión a internet si no la hay
while not is_connected() :
    print("No hay conexión a internet. Esperando {} segundos...".format(WAIT_TIME))
    time.sleep(WAIT_TIME)
    break

if  is_connected():
    # Guardar los datos en Firestore
    doc_name = 'data_' + str(sys.argv[1])
    db.collection('tfg').document(doc_name).set(data)

# Guardar los datos localmente si no hay conexión a internet
if not is_connected():
    save_local_data(filename, data)
