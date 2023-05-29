import gtts
from playsound import playsound
def reproduce_audio(text):
    tts = gtts.gTTS(text, lang="es",tld='es')
    tts.save("tmp.mp3")
    playsound("tmp.mp3")
    
    
reproduce_audio("Buenos días!! SOy el robot Pepper y seré hoy tu guía para la realización de este test. \
                Llamado el test de las palmeras y pirámides y consiste en que tú relaciones la imágen superior con solamente una de las imágenes\
                inferiores, ya sea la derecha o la izquierda, clicando con el dedo en ella.Puedes ver el ejemplo en pantalla. Durante las 3 primeras tríadas, te diré si los has hecho bien o no para\
                que entiendas la dinámica, luego, deberás continuar sola o solo. Muy bien!! Puedes clicar en empezar si la configuración ya ha sido introducida. Ánimo!!!")