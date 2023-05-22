#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from naoqi import ALProxy
import qi,subprocess,sys
#tablet=ALProxy("ALTabletService","127.0.0.1",9559)localhost:33945
"""

localhost:43397
"""
if len(sys.argv) < 2:
    print('Error: Debe ingresar IP:Port como argumento.')
    sys.exit()
IP_l= sys.argv[1].split(":")
tts=ALProxy("ALTextToSpeech",IP_l[0], int(IP_l[1]))
postura=ALProxy("ALRobotPosture",IP_l[0],int(IP_l[1]))


postura.goToPosture("Stand", 1.0)

# postura.goToPosture("Stand", 1.0)
try :
    vol=float(sys.argv[2])*0.01
    tts.setVolume(vol)
except:
    tts.setVolume(1)

print(tts.getVolume())
tts.say("Prueba de volumen")