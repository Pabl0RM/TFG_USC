import pygame
import pygame_menu,gtts
import json,subprocess
from pygame.locals import *
def escribir_archivo_texto( contenido):
    with open("media/tmp.txt", 'w') as archivo:
        archivo.write(str(contenido))
    print(f'Se ha creado y escrito en el archivo "{"tmp.txt"}".')
def reproduce_audio(text):
    tts = gtts.gTTS(text, lang="es",tld='es')
    tts.save("media/feedback.mp3")
    pygame.mixer.music.load('media/feedback.mp3')
    # Reproducir canción
    pygame.mixer.music.play()
    # Esperar a que termine la canción
    while pygame.mixer.music.get_busy():     
        continue    
def reproduce_audio2(prg):
    preguntas = [
    "¿El test es fácil de entender con el feedback sonoro?",
    "El input táctil es útil dentro del test realizado",
    "El feedback sonoro es útil dentro del test realizado",
    "Se entiende bien cuando se da feedback",
    "Seguiría un consejo de la app sobre el análisis del test",
    "¿Considera que un feedback sonoro le da valor añadido al test?" 
]
    tts = gtts.gTTS(preguntas[int(prg)], lang="es",tld='es')
    tts.save("media/feedback.mp3")
    pygame.mixer.music.load('media/feedback.mp3')
    # Reproducir canción
    pygame.mixer.music.play()
    # Esperar a que termine la canción
    while pygame.mixer.music.get_busy():     
        continue
def borrar_archivo_texto():
    import os
    if os.path.exists("media/tmp.txt"):
        with open("media/tmp.txt", 'r') as archivo:
            contenido = archivo.read()
            lista_contenido = contenido.split("\n")
            print(lista_contenido[:-1:])
        os.remove("media/tmp.txt")
        print(f'Se ha eliminado el archivo "{"tmp.txt"}".')
        return lista_contenido[:-1:]
    else:
        print(f'El archivo "{"tmp.txt"}" no existe.')
# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
X, Y =  pygame.display.set_mode().get_size()
screen = pygame.display.set_mode((X, Y))

# Crear un menú con Pygame-menu
menu = pygame_menu.Menu("Encuesta de usabilidad del robot Pepper", X, Y, theme=pygame_menu.themes.THEME_DARK )

# Lista de preguntas
preguntas = [
    "¿El test es fácil de entender con la ayuda del robot Pepper?",
    "El input táctil es útil dentro del test realizado",
    "¿El robot Pepper es útil dentro del test realizado?",
    "El robot transmite confianza cuando da feedback",
    "Seguiría un consejo del Pepper sobre el análisis del test",
 "¿Considera que el Pepper le da valor añadido al test?"   
]
preguntas2 = [
    "¿El test es fácil de entender con el feedback sonoro?",
    "El input táctil es útil dentro del test realizado",
    "El feedback sonoro es útil dentro del test realizado",
    "Se entiende bien cuando se da feedback",
    "Seguiría un consejo de la app sobre el análisis del test",
    "¿Considera que un feedback sonoro le da valor añadido al test?" 
]
respuestas=[None]*6

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
        #print("escrito",file_data)
# Función para mostrar la pregunta actual
def show_question():
    menu.clear()
    IP_port=open('media/tmpp.txt').read()
    if IP_port=="no":menu.add.label(preguntas2[current_question], font_size=70)
    else:menu.add.label(preguntas[current_question], font_size=70)
    menu.add.selector("Puntua", [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)], onchange=on_answer_change, font_size=100)
    if current_question!=0:
        menu.add.button("Anterior", previous_question, font_size=100)

    if current_question == len(preguntas) - 1:
        menu.add.button("Enviar", imprimir_respuestas, font_size=100)
    else:
        menu.add.button("Siguiente", next_question, font_size=100)        
    menu.add.button("Salir", fin, font_size=100)
    

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
    # IP_port=open('media/tmpp.txt').read()
    # subprocess.run(["python", "media/pepper_dice3.py",IP_port,str(current_question)])    
    show_question()
    
    IP_port=open('media/tmpp.txt').read()
    if IP_port!="no":subprocess.run(["python", "media/pepper_dice3.py",IP_port,str(current_question),volu])     
    else:reproduce_audio2(str(current_question))
# Función para pasar a la siguiente pregunta
def next_question():
    global current_question
    if current_question < len(preguntas) - 1:
        current_question += 1
    # IP_port=open('media/tmpp.txt').read()
    # subprocess.run(["python", "media/pepper_dice3.py",IP_port,str(current_question)]) 
    show_question()
    
    IP_port=open('media/tmpp.txt').read()
    if IP_port!="no":subprocess.run(["python", "media/pepper_dice3.py",IP_port,str(current_question),volu])     
    else:reproduce_audio2(str(current_question))   
def fin():
    IP_port=open('media/tmpp.txt').read()
    
    if IP_port!="no":subprocess.run(["python", "feedbackPepper-tablet/pepperAgradece.py",IP_port,volu])    
    else:reproduce_audio("El test y preguntas ya han finalizado. Muchísimas gracias por participar y espero que todo haya sido de tu agrado!!")       
    pygame.quit()
    quit()    
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
        print(j["name"])
        subprocess.run(["python3", "firebase_waits.py",j["name"]])        
        IP_port=open('media/tmpp.txt').read()
        subprocess.run(["python", "feedbackPepper-tablet/pepperAgradece.py",IP_port,volu])
        pygame.quit()
        quit()
     

# Mostrar la primera pregunta

show_question()

# Bucle principal del juego
def main(vol):
    global volu
    volu=vol
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
    main('90')
