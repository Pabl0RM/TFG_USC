# import pygame
# import pygame_menu
# from pygame.locals import *
# global lang,valor,value
# valor=dict(zip(["¿El robot Pepper es fácil de usar?", \
#                  "¿El robot Pepper es atractivo visualmente?", \
#                  "¿El robot Pepper es útil?", \
#                  "¿El robot Pepper es confiable?", \
#                  "¿El robot Pepper es fácil de entender?"],[0]*5))
# def encuesta():
#     # Inicializar Pygame
#     pygame.init()   

#     # Tamaño de la ventana
#     ventana_ancho, ventana_alto = 1000, 600
#     def answerr(value, eleccion):
        
#         # lang=difficulty
#         print('a1',eleccion)
#         print('b',value)
#         print('x',selector_id)
#         valor[selector_id]=eleccion
#         print(selector_id+" "+str(valor[selector_id]))
        
 
#     # Crear la encuesta
#     def survey_results(result):
#         respuestas = [("¿El robot Pepper es fácil de usar?"), 
#                       ("¿El robot Pepper es atractivo visualmente?"), 
#                       ("¿El robot Pepper es útil?"), 
#                       ("¿El robot Pepper es confiable?"), 
#                       ("¿El robot Pepper es fácil de entender?")]
#         print("Resultados de la encuesta:")
#         for pregunta in respuestas:
#             print(f"{pregunta}: {valor[pregunta]}")
#         return respuestas

#     # Crear la ventana y la superficie
#     ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
#     superficie = pygame.display.get_surface()

#     # Crear el menú de la encuesta
#     encuesta_menu = pygame_menu.Menu("Encuesta de usabilidad del robot Pepper", ventana_ancho, ventana_alto, theme=pygame_menu.themes.THEME_DARK)

#     # Agregar las preguntas a la encuesta
#     preguntas = ["¿El robot Pepper es fácil de usar?", 
#                  "¿El robot Pepper es atractivo visualmente?", 
#                  "¿El robot Pepper es útil?", 
#                  "¿El robot Pepper es confiable?", 
#                  "¿El robot Pepper es fácil de entender?"]

#     # Agregar las opciones de respuesta a la encuesta
#     opciones_respuesta = [("Muy en desacuerdo", 1), ("En desacuerdo", 2), ("Ligeramente en desacuerdo", 3), ("Neutral", 4), ("Ligeramente de acuerdo", 5), ("De acuerdo", 6), ("Muy de acuerdo", 7)]

#     # Agregar las preguntas a la encuesta con las opciones de respuesta
#     encuesta_menu.add.label("")
#     global selector_id
    
#     for pregunta in preguntas:
#         selector_id=pregunta
#         # encuesta_menu.add.label(pregunta)
#         encuesta_menu.add.selector(pregunta, opciones_respuesta, onchange=answerr, selector_id=pregunta)

#     # Agregar el botón para enviar la encuesta
#     encuesta_menu.add.label("")
#     encuesta_menu.add.button("Enviar", survey_results, pygame_menu.events.BACK)
#     encuesta_menu.add.button("Salir", pygame_menu.events.EXIT)

#     # Ejecutar la encuesta
#     encuesta_menu.mainloop(superficie)

# if __name__ == "__main__":
#     encuesta()


import pygame,sys,os
import pygame_menu
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
            print(lista_contenido)
        os.remove("tmp.txt")
        print(f'Se ha eliminado el archivo "{"tmp.txt"}".')
        return lista_contenido
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
        resp+=str(data[i])+str(respuesta[data2[i]][0][0])+"\n"
    
    escribir_archivo_texto(resp)
    respuestas=borrar_archivo_texto()
    for i in respuestas:
        if i!='':print(i[1])

# Agregar botones al menú
menu.add.button('Enviar', imprimir_respuestas)
menu.add.button('Salir', pygame_menu.events.EXIT)

# Bucle principal del juego
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
