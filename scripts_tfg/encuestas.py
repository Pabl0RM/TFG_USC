import pygame,sys,os,subprocess
import pygame_menu,json


# ID_enmcr='error'
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
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Crear un menú con Pygame-menu
menu = pygame_menu.Menu("Encuesta de usabilidad del robot Pepper", SCREEN_HEIGHT, SCREEN_WIDTH, theme=pygame_menu.themes.THEME_DARK)


# Lista de preguntas
preguntas = ["¿El robot Pepper es fácil de usar?", 
                 "¿El robot Pepper es atractivo visualmente?", 
                 "¿El robot Pepper es útil?", 
                 "¿El robot Pepper es confiable?", 
                 "¿El robot Pepper es fácil de entender?"]

# Agregar opciones para cada pregunta
for pregunta in preguntas:
    menu.add.selector(pregunta, [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])


# Función para imprimir las respuestas
def imprimir_respuestas():
    data=[ii for ii,e in enumerate(menu.get_input_data())]
    data2=[e for ii,e in enumerate(menu.get_input_data())]
    
    # print(data)
    # print(data2)
    resp=''
    for i, pregunta in enumerate(preguntas):
        respuesta = menu.get_input_data()
        # print(data[i])
        # print(data2[i])
        # # respuesta[data[i]] = respuesta.pop(data2[i])
        # print(respuesta)
        print(pregunta+' '+str(respuesta[data2[i]][0][0]))
        # resp+=str(data[i])+str(respuesta[data2[i]][0][0])+"\n"
        resp+=str(respuesta[data2[i]][0][0])+"\n"
    
    escribir_archivo_texto(resp)
    
    #print(borrar_archivo_texto())
    respuestas=borrar_archivo_texto()
    # print(respuestas)
    f = open('ST_data.json')
    j=json.load(f)
    # print(j)
    # print(j["name"])
    #input()
    subprocess.run(["python3", "firebase_waits.py",j["name"]])
    
    pygame.quit()
    quit()

# Agregar botones al menú
menu.add.button('Enviar', imprimir_respuestas)
menu.add.button('Salir', pygame_menu.events.EXIT)

# Bucle principal del juego
def main():

    while True:
        # Manejar eventos de Pygame
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

        # Dibujar el menú
        screen.fill((0, 0, 0))
        menu.update(events)
        menu.draw(screen)

        # Actualizar la pantalla
        pygame.display.update()
# main()

