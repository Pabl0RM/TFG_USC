#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from naoqi import ALProxy
import qi
#tablet=ALProxy("ALTabletService","127.0.0.1",9559)localhost:33945
"""

localhost:42067
localhost:34537
"""
tts=ALProxy("ALAnimatedSpeech","localhost", 34537)
postura=ALProxy("ALRobotPosture","localhost", 34537)


postura.goToPosture("Stand", 1.0)
tts.say("Buenos dias!!")


tts.say("Bienvenido al test semántico, procedo a realizar una breve explicación")
# postura.goToPosture("Stand", 1.0)
tts.say("La memoria semántica es definida como el\
        sistema que permite almacenar el significado de\
        las palabras, objetos, conceptos y el significado\
        del mundo en general. El test más utilizado paraevaluar los déficit semánticos adquiridos es elTest de Pirámides y Palmeras . Es una prueba de asociación semántica que se administra desde diferentes modalidades (pictórica y verbal) y se encuentra muy condicionada por el medio socio cultural.")

# class StateMachine:
    
#     def __init__(self):
#         self.handlers = {}
#         self.startState = None
#         self.endStates = []

#     def add_state(self, name, handler, end_state=0):
#         name = name.upper()
#         self.handlers[name] = handler    
#         if end_state:
#             self.endStates.append(name)

#     def set_start(self, name):
#         self.startState = name.upper()

#     def run(self, cargo):
#         try:
#             handler = self.handlers[self.startState]
#         except:
#             raise InitializationError("debes llamar al metodo .set_start() antes de .run()")
#         if not self.endStates:
#             raise  InitializationError("como minimo un estado debe ser el final")
    
#         while True:
#             (newState, cargo) = handler(cargo)
#             if newState.upper() in self.endStates:
#                 print("llegamos ", newState)
#                 break 
#             else:
#                 handler = self.handlers[newState.upper()]   
# positive_adjectives = ["genial","bien", "divertido", "entretenido", "facil","si"]
# negative_adjectives = ["aburrido", "dificil", "feo", "malo","mal",'No','no']
# preguntas=['Que tal te ha ido?','Como fue la exp?','En general, se adecuo a tus expectativas?','Si no es indiscreccion, podrias valorar la estancia?'\
#     ,'Que te llevas de la experiencia?']
# respuestas=["siSisiSivaleValevengaVenga","Nono"]
# def start_transitions(txt):
#     print('Estado start')
#     splitted_txt = txt.split(None,1)
#     word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
#     if word in respuestas[0]:
#         newState = "chat_state"
        
#         s=random.choice(preguntas)
#         print(s)
#         tts.say('\\vol=20\\'+s)
        
#         txt=raw_input("R:")

#         # txt=text_reg()


#     elif word in respuestas[1]:
#         newState = "estado_fin"
#     else:
#         print("No le he entedido, repito:")
#         tts.say('\\vol=20\\No le he entedido, repito:\n')
        
#         newState = "estado_error_indecision"
#     return (newState, txt)

# def chat_state_transitions(txt):
#     # print(txt)
#     print('Estado chat')
#     splitted_txt = txt.split(None,1)
    
#     word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
#     if 1==1:
#         newState = "Start"
#         print('Genial, muchas gracias. Buen día\n')
#         tts.say('\\vol=20\\Genial, muchas gracias. Buen dia\n')
#         #tablet.showImage('indice.jpeg')
#         txt=raw_input('Más preguntas?')
#         # txt=text_reg()
#     else:
#         newState = "estado_error_indecision"
#         tts.say('\\vol=20\\Podria hacerte otra pregunta?\n')
#         txt=raw_input('Podría hacerte otra pregunta?\n')
#         # txt=text_reg()
#     return (newState, txt)


# def estado_indecision(txt):
#     print('-------------------\nEstado indecision\n-------------------')
#     splitted_txt = txt.split(None,1)
#     tts.say('\\vol=20\\Buenas tardes, podria hacerle unas preguntas, sobre satistaccion?')
#     word=raw_input('Buenas tardes, podría hacerle unas preguntas, sobre satistaccion?\n')
#     # word=text_reg()
#     # word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
#     if word in respuestas[1]:
#         newState = "estado_error"
#     elif word in respuestas[0]:
#         # print('\n-------------------\nEstado indecision, repito pregunta\n-------------------\n')
#         newState = "Start"

#     else:
#         c=+1
#         if c<5:
#             newState = "estado_error_indecision"
#         else:
#             newState="estado_error"
#     return (newState, txt)


# m = StateMachine()
# m.add_state("Start", start_transitions)
# m.add_state("chat_state", chat_state_transitions)
# # m.add_state("1_state", one_state_transitions)
# # m.add_state("0_state", z_state_transitions)
# m.add_state("estado_error_indecision", estado_indecision)
# m.add_state("estado_fin", None, end_state=1)
# m.add_state("estado_error", None, end_state=1)
# m.set_start("Start")
# tts.say('\\vol=20\\Buenas tardes, podria hacerle unas preguntas, sobre satistaccion?')
# # txt=text_reg()
# I=str(raw_input('Buenas tardes, podría hacerle unas preguntas, sobre satistaccion?\n'))
# # I=text_reg()
# # I="si"
# m.run(I)
 