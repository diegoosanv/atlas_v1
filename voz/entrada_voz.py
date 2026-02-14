import speech_recognition as sr

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Escuchando...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio, language="es-MX")
    except:
        return ""
