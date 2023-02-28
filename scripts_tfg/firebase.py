import pandas as pd,os
import firebase_admin,json,sys
from firebase_admin import credentials, firestore

if len(sys.argv) < 2:
    print('Error: Debe ingresar el ID del paciente.')
    sys.exit()

cred = credentials.Certificate("tfg-data-173bc-firebase-adminsdk-9ixg4-59eb87bd6d.json")
firebase_admin.initialize_app(cred, 
{
'databaseURL': 'https://tfg.firebaseio.com/'
})
db = firestore.client()
#exporta datos

with open('ST_data.json') as f:
    data = json.load(f)

db.collection('tfg').document('data_' + str(sys.argv[1])).set(data)