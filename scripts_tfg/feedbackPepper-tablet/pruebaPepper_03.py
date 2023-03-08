#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from naoqi import ALProxy
import qi
#tablet=ALProxy("ALTabletService","127.0.0.1",9559)localhost:33945
"""

localhost:42067
"""
tts=ALProxy("ALAnimatedSpeech","localhost", 34537)
postura=ALProxy("ALRobotPosture","localhost", 34537)


postura.goToPosture("Stand", 1.0)

# postura.goToPosture("Stand", 1.0)
tts.say("Efectivamente!! ESa era la imagen adecuada")
