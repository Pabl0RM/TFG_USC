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
tts=ALProxy("ALAnimatedSpeech",IP_l[0], int(IP_l[1]))
postura=ALProxy("ALRobotPosture",IP_l[0],int(IP_l[1]))



postura.goToPosture("Stand", 1.0)
preguntas = [
    "¿El robot Pepper es fácil de usar?",
    "¿El robot Pepper es atractivo visualmente?",
    "¿El robot Pepper es útil?",
    "¿El robot Pepper es confiable?",
    "¿El robot Pepper es fácil de entender?"
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