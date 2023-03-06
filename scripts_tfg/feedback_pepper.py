from naoqi import ALProxy
import sys

# Conexión al robot

ip = "localhost"
port = 32871
motion_service = ALProxy("ALMotion", ip, port)
posture_service = ALProxy("ALRobotPosture", ip, port)
tts = ALProxy("ALTextToSpeech", ip, port)

# Hacer que el robot se sorprenda
motion_service.setAngles(["HeadYaw", "HeadPitch", "RShoulderPitch", "RElbowRoll", "RWristYaw"],
                         [0.0, 0.0, -1.5, -0.5, 1.0], 0.1)

# Seleccionar el mensaje en función de los argumentos de entrada
if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = "Buenos días"

if message == "Buenos días":
    tts.say("Buenos días")
elif message == "Buenas tardes":
    tts.say("Buenas tardes")
elif message == "Adiós":
    tts.say("Adiós")
else:
    tts.say("No entiendo lo que quieres decir.")

# Cambiar la postura del robot
posture_service.goToPosture("StandInit", 0.5)
     