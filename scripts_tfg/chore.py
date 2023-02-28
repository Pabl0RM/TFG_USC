class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        
        import random
        # import speech_recognition as sr

        
        from naoqi import ALProxy
        #from naoqi import ALRobotPostureProxy
        import qi
        
        #tablet=ALProxy("ALTabletService","127.0.0.1",9559)localhost:65332localhost:41963
        #localhost:38265
        tts=ALProxy("ALTextToSpeech","localhost", 38265)
        # tts.say("esto es una pasada")localhost:43933localhost:49236
        #Esta parte del codigo permite que el robot se levante..."192.168.0.107"
        postura=ALProxy("ALRobotPosture","localhost", 38265)
        
        tts.say("Buenos dias, bienvenidos al test semántico.")
        postura.goToPosture("Stand",1.0)
        tts.say("La memoria semántica es definida como el\
        sistema que permite almacenar el significado de\
        las palabras, objetos, conceptos y el significado\
        del mundo en general. El test más utilizado para\
        eva luar los déficit semánticos adquiridos es el\
        Test de Pirámides y Palmeras . Es una prueba de asociación semántica\
        que se administra desde diferentes modalidades\
        (pictórica y verbal) y se encuentra\
        muy condicionada por el medio socio cultural.")
        
        postura.goToPosture("Crouch",1.0)
        

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
