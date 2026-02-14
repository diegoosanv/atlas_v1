import queue, json

import sounddevice as sd

from vosk import Model, KaldiRecognizer


MODEL_PATH = "voz/modelo_vosk"

q = queue.Queue()


def callback(indata, frames, time, status):

    q.put(bytes(indata))


def escuchar():

    model = Model(MODEL_PATH)

    rec = KaldiRecognizer(model, 16000)


    with sd.RawInputStream(

        samplerate=16000,

        blocksize=8000,

        dtype="int16",

        channels=1,

        callback=callback

    ):

        while True:

            data = q.get()

            if rec.AcceptWaveform(data):

                texto = json.loads(rec.Result()).get("text", "")
                print("ESCUCHE:", texto)

                if texto:

                    return texto.lower()




