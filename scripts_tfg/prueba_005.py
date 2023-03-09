from time import sleep
import pygame,os,subprocess,sys
import pygame_menu
from pygame_menu import themes
from pygame.locals import *
from game_test import mmain
import speech_recognition as sr
import gtts
from playsound import playsound
import hashlib
import random
global count_down,seconds
count_down = 5
seconds=0

global Name,lang
Name='';lang=''
# Crea una fuente personalizada con tamaño 10
my_font = pygame_menu.font.FONT_OPEN_SANS

# Crea el tema con la fuente personalizada
my_theme = pygame_menu.themes.Theme(
    background_color=(228, 230, 246),
    scrollbar_shadow=True,
    scrollbar_slider_color=(150, 200, 230),
    scrollbar_slider_hover_color=(123, 173, 202),
    scrollbar_slider_pad=2,
    selection_color=(100, 62, 132),
    title_background_color=(62, 149, 195),
    title_font_color=(228, 230, 246),
    title_font_shadow=True,
    widget_font_color=(61, 170, 220),
    title_font_size=150,
    widget_font_size=150

)
# Definir la versión del juego
VERSION = "1.0"



pygame.init()
X=1900

Y=1060


X,Y = pygame.display.set_mode().get_size()

surface = pygame.display.set_mode((X, Y),RESIZABLE)
# Configurar el temporizador
clock = pygame.time.Clock()
start_ticks = 0



def reproduce_audio(text):
    tts = gtts.gTTS(text, lang="es",tld='es')
    tts.save(text[0]+".mp3")
    playsound(text[0]+".mp3")
    
    









def set_leguage(value, difficulty):
    global lang
    lang=difficulty
    print(difficulty)
    
def name():
    #extraer nombre, speech recog

    #uso del micro
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Escoitamos o que di o usuario co micro por defecto do equipo
    print("¡Te escucho!")
    
    reproduce_audio('Buenos dias, dime tu nombre')
    with mic as source:
        audio = r.listen(source)
    
    # Transcribimos o audio a texto
    text = r.recognize_google(audio, language='es-ES')
    print("Creo que has dicho: \"" + text + "\"")

    # Xeramos un novo discurso sintético a partir do texto anterior
    tts = gtts.gTTS(text, lang="es")
    tts.save("name.mp3")
    playsound("name.mp3")
    global Name
    Name=text

    # Name="pablo"
    print(Name)
    
    # TODO funciones con ALSpeechRecognition para pepper?
    


def token(length=12):


    """Genera un token único de 30 caracteres como máximo."""
    chars = list(
        'ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz01234567890'
    )
    random.shuffle(chars)
    chars = ''.join(chars)
    sha1 = hashlib.sha1(chars.encode('utf8'))
    token = sha1.hexdigest()
    return token[:length] 

def start_countdown():
    global start_ticks
    start_ticks = pygame.time.get_ticks()

# Función para actualizar el temporizador
def update_timer():
    global seconds
    total_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    seconds = total_seconds % 60
    timer_text =  str(5 - seconds) + "s"
    timer_label.set_title(timer_text)    
    
def start_the_game():
    mainmenu._open(loading)
    start_countdown()
    pygame.time.set_timer(update_loading, 30)
 
def level_menu():
    mainmenu._open(level)
def explicacion_pepper():
    # subprocess.Popen("python pruebaPepper_01.py ", shell=True) 
    subprocess.run(["python", "feedbackPepper-tablet/pruebaPepper_01.py",IP_port])
    
def explicacion_sintetizador():
    pygame.mixer.music.load('tmp.mp3')

# Reproducir canción
    pygame.mixer.music.play()

    # Esperar a que termine la canción
    while pygame.mixer.music.get_busy():
        continue

def pepper_config(v):
    global IP_port
    IP_port=v
    print(IP_port)

def option_menu():
    mainmenu._open(options)
 
def rest():
    print(Name)
mainmenu = pygame_menu.Menu('TFG', X, Y, theme=my_theme)


mainmenu.add.button("Nombre ", name,font_size=100)
mainmenu.add.button('Empezar', start_the_game, font_size=100)
mainmenu.add.button('Explicacion', level_menu, font_size=100)
mainmenu.add.button('Opciones', option_menu, font_size=100)
mainmenu.add.button('Salir', pygame_menu.events.EXIT, font_size=100)
mainmenu.add.label('Version1.0',font_size=20)


level = pygame_menu.Menu('Descripcion del test', X, Y, theme=my_theme)
level.add.button('Pepper',explicacion_pepper, font_size=100)
# level.add.button('Terminal-Sintetizador',explicacion_sintetizador)
level.add.button('Terminal-Sintetizador',explicacion_sintetizador, font_size=100)



options = pygame_menu.Menu('Opciones', X, Y, theme=my_theme)
options.add.selector('Idioma :', [('Español', "esp"), ('Inglés', "eng"), ('Galego', "gal")], onchange=set_leguage,font_size=100) 
options.add.button('Nombre', rest, button_id='namee', font_size=100)
options.add.text_input("IP:port-> ", default="", onchange=pepper_config,font_size=100)


options.add.range_slider('Selector', 50, (0, 100), 1,
                      rangeslider_id='range_slider',
                      value_format=lambda x: str(int(x)), width = 200,font_size=100)



 
loading = pygame_menu.Menu('Cargando el test...', X, Y, theme=my_theme)

timer_label = loading.add.label('5s', font_size=100)
 
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (20, 30))
 
update_loading = pygame.USEREVENT + 0
 

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:


            pygame.time.set_timer(pygame.USEREVENT+1, 1000)
            # Actualizar el temporizador
            if start_ticks > 0:
                update_timer()
                # subprocess.Popen("python prueba_004.py ", shell=True)  
                # subprocess.run(["python", "prueba_004.py"])
                if seconds==5:
                    mmain(token(),lang,VERSION,IP_port)
                    exit()             
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
             arrow.draw(surface, mainmenu.get_current().get_selected_widget())
 
    pygame.display.update()