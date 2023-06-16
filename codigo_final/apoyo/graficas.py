import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import matplotlib.pyplot as plt
import numpy as np

# Ruta al archivo de configuración JSON generado en Firebase
cred = credentials.Certificate("tfg-data-173bc-firebase-adminsdk-9ixg4-59eb87bd6d.json")

# Inicializar la aplicación de Firebase
firebase_admin.initialize_app(cred)

# Obtener una instancia de Firestore
db = firestore.client()

# Obtener una referencia a la colección "tfg"
coleccion = db.collection('tfg')

ultimos_documentos = coleccion.order_by("time_stamp", direction=firestore.Query.DESCENDING).limit(5).get()
print(ultimos_documentos)
# Listas para almacenar los valores de aciertos, fallos y omisiones
aciertos = []
fallos = []
omisiones = []
# ultimos_documentos = ultimos_documentos[1:]
# Iterar sobre los documentos y guardar los valores en las listas
for documento in ultimos_documentos:
    datos = documento.to_dict()
    aciertos.append(datos['aciertos'])
    fallos.append(datos['fallos'])
    omisiones.append(datos['omisiones'])
aciertos=aciertos[::-1]
fallos=fallos[::-1]
omisiones=omisiones[::-1]
# Configurar la gráfica de barras
# categorias = ['P.1', 'P.2', 'P.3', 'P.4', 'P.5',
#               'P.6', 'P.7', 'P.8', 'P.9', 'P.10']
categorias = ['P.1', 'P.2', 'P.3', 'P.4', 'P.5']
plt.style.use(['science','no-latex'])
bar_width = 0.2
index = np.arange(len(categorias))

plt.bar(index, aciertos, bar_width, label='Aciertos', color="green")
plt.bar(index + bar_width, fallos, bar_width, label='Fallos', color="red")
plt.bar(index + (2 * bar_width), omisiones, bar_width, label='Omisiones', color="grey")

plt.xlabel('Personas')
plt.ylabel('Resultados')
plt.title('Resultados de las 5 personas que realizaron el test textual')
plt.legend()

plt.xticks(index + bar_width, categorias)
plt.tight_layout()

plt.show()

# Finalizar la aplicación de Firebase
firebase_admin.delete_app(firebase_admin.get_app())










# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# import matplotlib.pyplot as plt
# import numpy as np

# # Ruta al archivo de configuración JSON generado en Firebase
# cred = credentials.Certificate("tfg-data-173bc-firebase-adminsdk-9ixg4-59eb87bd6d.json")

# # Inicializar la aplicación de Firebase
# firebase_admin.initialize_app(cred)

# # Obtener una instancia de Firestore
# db = firestore.client()

# # Obtener una referencia a la colección "tfg"
# coleccion = db.collection('tfg')

# # Obtener los últimos 10 documentos subidos
# ultimos_documentos = coleccion.order_by('time_stamp', direction=firestore.Query.DESCENDING).limit(11).get()

# # Lista para almacenar los valores de respuestas
# respuestas = []
# # respuestas=respuestas[]
# # Iterar sobre los documentos y guardar los valores en la lista
# for documento in ultimos_documentos:
#     datos = documento.to_dict()
#     respuestas.append(datos['respuestas'].split(" "))

# respuestas = [[int(valor) for valor in fila] for fila in respuestas]

# # Configurar el tamaño de la figura
# plt.figure(figsize=(12, 8))
# plt.style.use(['science','no-latex'])
# plt.title("Respuestas de la encuesta de satisfacción")

# # Colores para las barras en cada subfigura
# colores = ["red", "green", "blue", "orange", "purple"]

# # Iterar sobre cada sublista
# for i, sublist in enumerate(respuestas):
#     # Convertir los elementos de cadena de texto a números enteros
#     sublist_numeros = [int(valor) for valor in sublist]
    
#     # Etiquetas para cada quesito
#     etiquetas = ['Prg.1', 'Prg.2', 'Prg.3', 'Prg.4', 'Prg.5', 'Prg.6']
    
#     # Plotear el gráfico de barras
#     plt.subplot(2, 5, i+1)
#     plt.bar(etiquetas, sublist_numeros, color=colores[i % len(colores)])
#     plt.title(f'Persona {abs(i-10)}')

#     # Configurar el color de las barras individuales
#     for j, barra in enumerate(plt.gca().patches):
#         barra.set_color(colores[j % len(colores)])

# # Ajustar el espaciado entre los subplots
# plt.tight_layout()

# # Mostrar los gráficos
# plt.show()

# # Finalizar la aplicación de Firebase
# firebase_admin.delete_app(firebase_admin.get_app())

