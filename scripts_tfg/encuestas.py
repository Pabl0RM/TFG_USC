import pygame
import pygame_menu
from pygame.locals import *
def main():
    # Inicializar Pygame
    pygame.init()
    X,Y = pygame.display.set_mode().get_size()

    surface = pygame.display.set_mode((X, Y),RESIZABLE)

    # Crear la encuesta

    def survey_results(result, data):
        print(f"Resultados de la encuesta: {result}")
        print(f"Datos adicionales: {data}")
        

    survey_menu = pygame_menu.Menu("Encuesta de satisfacción", X, Y, theme=pygame_menu.themes.THEME_DARK)

    # Agregar las preguntas a la encuesta
    question1 = "¿Está satisfecho con nuestro servicio?"
    question2 = "¿Recomendaría nuestro servicio a otros?"
    question3 = "¿Cómo evalúa la calidad de nuestro servicio?"
    question4 = "¿El tiempo de respuesta de nuestro servicio fue adecuado?"
    question5 = "¿Fue fácil de usar nuestro servicio?"

    # Agregar las opciones de respuesta a la encuesta
    likert_options = [("1 - Muy insatisfecho", 1), ("2 - Insatisfecho", 2), ("3 - Neutral", 3), ("4 - Satisfecho", 4), ("5 - Muy satisfecho", 5)]

    # Agregar las preguntas a la encuesta con las opciones de respuesta
    survey_menu.add.label(question1)
    survey_menu.add.selector("", likert_options, onchange=None)
    survey_menu.add.label(question2)
    survey_menu.add.selector("", likert_options, onchange=None)
    survey_menu.add.label(question3)
    survey_menu.add.selector("", likert_options, onchange=None)
    survey_menu.add.label(question4)
    survey_menu.add.selector("", likert_options, onchange=None)
    survey_menu.add.label(question5)
    survey_menu.add.selector("", likert_options, onchange=None)

    # Agregar un campo de texto para datos adicionales
    survey_menu.add.label("")
    survey_menu.add.label("--Datos adicionales--")
    survey_menu.add.text_input("Comentarios", default="")

    # Agregar el botón para enviar la encuesta
    survey_menu.add.button("Enviar", survey_results, pygame_menu.events.EXIT)
    survey_menu.add.button('Salir', pygame_menu.events.EXIT)
    # Ejecutar la encuesta
    survey_menu.mainloop(surface)

main()