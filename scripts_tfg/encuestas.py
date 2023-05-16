import pygame
import pygame_menu
import json,subprocess
def escribir_archivo_texto( contenido):
    with open("tmp.txt", 'w') as archivo:
        archivo.write(str(contenido))
    print(f'Se ha creado y escrito en el archivo "{"tmp.txt"}".')

def borrar_archivo_texto():
    import os
    if os.path.exists("tmp.txt"):
        with open("tmp.txt", 'r') as archivo:
            contenido = archivo.read()
            lista_contenido = contenido.split("\n")
            print(lista_contenido[:-1:])
        os.remove("tmp.txt")
        print(f'Se ha eliminado el archivo "{"tmp.txt"}".')
        return lista_contenido[:-1:]
    else:
        print(f'El archivo "{"tmp.txt"}" no existe.')
# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
X, Y = 800, 600
screen = pygame.display.set_mode((X, Y))

# Crear un menú con Pygame-menu
menu = pygame_menu.Menu("Encuesta de usabilidad del robot Pepper", X, Y, theme=pygame_menu.themes.THEME_DARK)

# Lista de preguntas
preguntas = [
    "¿El robot Pepper es fácil de usar?",
    "¿El robot Pepper es atractivo visualmente?",
    "¿El robot Pepper es útil?",
    "¿El robot Pepper es confiable?",
    "¿El robot Pepper es fácil de entender?"
]
respuestas=[None]*5

# Variable para controlar el índice de la pregunta actual
current_question = 0
def write_json(new_data, filename='ST_data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["respuestas"]=(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json
        json.dump(file_data, file, indent = 4)
# Función para mostrar la pregunta actual
def show_question():
    menu.clear()
    menu.add.label(preguntas[current_question])
    menu.add.selector("Puntua", [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)], onchange=on_answer_change)
    menu.add.button("Anterior", previous_question)
    menu.add.button("Siguiente", next_question)
    if current_question == len(preguntas) - 1:
        menu.add.button("Enviar", imprimir_respuestas)
    menu.add.button("Salir", pygame_menu.events.EXIT)
    

# Función para manejar el cambio de respuesta
def on_answer_change(value, index):
    
   
    # Guardar la respuesta en algún lugar (puedes usar una lista, diccionario, etc.)
    # Por ejemplo, puedes crear una lista llamada 'respuestas' fuera de esta función y hacer:
    respuestas[current_question]=index
    pass

# Función para pasar a la pregunta anterior
def previous_question():
    global current_question
    if current_question > 0:
        current_question -= 1
    # IP_port=open('tmpp.txt').read()
    # subprocess.run(["python", "pepper_dice3.py",IP_port,str(current_question)])    
    show_question()
    
    IP_port=open('tmpp.txt').read()
    subprocess.run(["python", "pepper_dice3.py",IP_port,str(current_question)])     
    
# Función para pasar a la siguiente pregunta
def next_question():
    global current_question
    if current_question < len(preguntas) - 1:
        current_question += 1
    # IP_port=open('tmpp.txt').read()
    # subprocess.run(["python", "pepper_dice3.py",IP_port,str(current_question)]) 
    show_question()
    
    IP_port=open('tmpp.txt').read()
    subprocess.run(["python", "pepper_dice3.py",IP_port,str(current_question)])     

# Función para imprimir las respuestas
def imprimir_respuestas():

        # Obtener todas las respuestas guardadas

        resp=''
        for i, pregunta in enumerate(preguntas):

            # # respuesta[data[i]] = respuesta.pop(data2[i])
            print(respuestas)
            print(pregunta+' '+str(respuestas[i]))
            # resp+=str(data[i])+str(respuesta[data2[i]][0][0])+"\n"
            resp+=str(respuestas[i])+"\n"

        # Aquí puedes hacer lo que necesites con las respuestas (guardar en archivo, enviar a servidor, etc.)
        # escribir_archivo_texto(resp)
        # respuestas=borrar_archivo_texto()
        # print(respuestas)
        print(resp)
        write_json(resp)
        f = open('ST_data.json')
        j=json.load(f)
        #input()

        subprocess.run(["python3", "firebase_waits.py",j["name"]])        
        pygame.quit()
        quit()
     

# Mostrar la primera pregunta

show_question()

# Bucle principal del juego
def main():
    while True:
        # Manejar eventos de Pygame
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Dibujar el menú
        screen.fill((0, 0, 0))
        menu.update(events)
        menu.draw(screen)
    
        # Actualizar la pantalla
        pygame.display.update()

# Llamar a la función principal
if __name__ == "__main__":
    main()
