import gtts
from playsound import playsound
def reproduce_audio(text):
    tts = gtts.gTTS(text, lang="es",tld='es')
    tts.save("tmp.mp3")
    playsound("tmp.mp3")
    
    
reproduce_audio('Prueba de sintetizador')