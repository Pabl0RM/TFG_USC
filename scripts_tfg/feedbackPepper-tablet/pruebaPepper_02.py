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
    print('Error: Debe ingresar el nombre del archivo JSON como argumento.')
    sys.exit()
IP_l= sys.argv[1].split(":")
tts=ALProxy("ALAnimatedSpeech",IP_l[0], int(IP_l[1]))
postura=ALProxy("ALRobotPosture",IP_l[0],int(IP_l[1]))



postura.goToPosture("Stand", 1.0)

# postura.goToPosture("Stand", 1.0)
tts.say("Vaya!!,Te has equivocado eligiendo la imagen")
