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
    print('Error: Debe ingresar IP:Port como argumento.')
    sys.exit()
IP_l= sys.argv[1].split(":")
tts=ALProxy("ALTextToSpeech",IP_l[0], int(IP_l[1]))
postura=ALProxy("ALRobotPosture",IP_l[0],int(IP_l[1]))

try :
    vol=float(sys.argv[2])*0.01
    tts.setVolume(vol)
except:
    tts.setVolume(1)

print(tts.getVolume())

postura.goToPosture("Stand", 1.0)

# postura.goToPosture("Stand", 1.0)
tts.say("El test y preguntas ya han finalizado. Muchísimas gracias por participar y espero que todo haya sido de tu agrado!!")
