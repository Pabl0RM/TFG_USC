import pygame
import pygame_menu
from pygame.locals import *

def encuesta():
    # Inicializar Pygame
    pygame.init()

    # Tamaño de la ventana
    ventana_ancho, ventana_alto = 800, 600
    def answerr(value, difficulty):
        global lang
        lang=difficulty
        print(difficulty)
        print(value)
        print(selector_id)
    # Crear la encuesta
    def survey_results(result):
        respuestas = [("¿El robot Pepper es fácil de usar?", result[0]), 
                      ("¿El robot Pepper es atractivo visualmente?", result[1]), 
                      ("¿El robot Pepper es útil?", result[2]), 
                      ("¿El robot Pepper es confiable?", result[3]), 
                      ("¿El robot Pepper es fácil de entender?", result[4])]
        print("Resultados de la encuesta:")
        for pregunta, respuesta in respuestas:
            print(f"{pregunta}: {respuesta}")
        return respuestas

    # Crear la ventana y la superficie
    ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
    superficie = pygame.display.get_surface()

    # Crear el menú de la encuesta
    encuesta_menu = pygame_menu.Menu("Encuesta de usabilidad del robot Pepper", ventana_ancho, ventana_alto, theme=pygame_menu.themes.THEME_DARK)

    # Agregar las preguntas a la encuesta
    preguntas = ["¿El robot Pepper es fácil de usar?", 
                 "¿El robot Pepper es atractivo visualmente?", 
                 "¿El robot Pepper es útil?", 
                 "¿El robot Pepper es confiable?", 
                 "¿El robot Pepper es fácil de entender?"]

    # Agregar las opciones de respuesta a la encuesta
    opciones_respuesta = [("Muy en desacuerdo", 1), ("En desacuerdo", 2), ("Ligeramente en desacuerdo", 3), ("Neutral", 4), ("Ligeramente de acuerdo", 5), ("De acuerdo", 6), ("Muy de acuerdo", 7)]

    # Agregar las preguntas a la encuesta con las opciones de respuesta
    encuesta_menu.add.label("")
    global selector_id
    
    for pregunta in preguntas:
        selector_id=pregunta
        encuesta_menu.add.label(pregunta)
        encuesta_menu.add.selector("", opciones_respuesta, onchange=answerr, selector_id=pregunta)

    # Agregar el botón para enviar la encuesta
    encuesta_menu.add.label("")
    encuesta_menu.add.button("Enviar", survey_results, pygame_menu.events.BACK)
    encuesta_menu.add.button("Salir", pygame_menu.events.EXIT)

    # Ejecutar la encuesta
    encuesta_menu.mainloop(superficie)

if __name__ == "__main__":
    encuesta()
