import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("voice", "spanish")

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()


