#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from naoqi import ALProxy
import qi,subprocess,sys
#tablet=ALProxy("ALTabletService","127.0.0.1",9559)localhost:33945
"""

localhost:42067
"""
if len(sys.argv) < 2:
    print('Error: Debe ingresar IP:port argumento.')
    sys.exit()
IP_l= sys.argv[1].split(":")
tts=ALProxy("ALTextToSpeech",IP_l[0], int(IP_l[1]))
postura=ALProxy("ALRobotPosture",IP_l[0],int(IP_l[1]))
try :
    vol=float(sys.argv[3])*0.01
    tts.setVolume(vol)
except:
    tts.setVolume(1)
print(tts.getVolume())

postura.goToPosture("Stand", 1.0)
preguntas = [
    "¿El test es fácil de entender con la ayuda del robot Pepper?",
    "El robot puede adaptarse al test realizado",
    "¿El robot Pepper es útil dentro del test realizado?",
    "El robot transmite confianza cuando da feedback",
    "Seguiría un consejo del Pepper sobre el análisis del test",
    "¿Considera que el Pepper le da valor añadido al test?" 
]
# postura.goToPosture("Stand", 1.0)
if   sys.argv[2]=='0':
    tts.say(preguntas[0])
elif sys.argv[2]=='1':
    tts.say(preguntas[1])
elif sys.argv[2]=='2':
    tts.say(preguntas[2])
elif sys.argv[2]=='3':    
    tts.say(preguntas[3])
elif sys.argv[2]=='4':    
    tts.say(preguntas[4])