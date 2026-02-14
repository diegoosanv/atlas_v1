

import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 170)


def hablar(texto):

    engine.say(texto)

    engine.runAndWait()

