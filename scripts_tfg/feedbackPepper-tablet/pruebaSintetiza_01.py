import gtts
from playsound import playsound
def reproduce_audio(text):
    tts = gtts.gTTS(text, lang="es",tld='es')
    tts.save("tmp.mp3")
    playsound("tmp.mp3")
    
    
reproduce_audio("La memoria semántica es definida como el\
        sistema que permite almacenar el significado de\
        las palabras, objetos, conceptos y el significado\
        del mundo en general. El test más utilizado paraevaluar los déficit semánticos adquiridos es elTest de Pirámides y Palmeras\
         . Es una prueba de asociación semántica que se administra desde diferentes modalidades (pictórica y verbal) y se encuentra muy \
                condicionada por el medio socio cultural.")