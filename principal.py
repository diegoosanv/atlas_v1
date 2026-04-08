import threading

import socket


from voz.stt import escuchar

from voz.tts import hablar

from vision.rostros import hay_persona


from ia.ollama_cliente import responder_offline

from ia.gemini_cliente import responder_gemini


from config import WAKE_WORD, USAR_CAMARA, USAR_TTS


from interfaz.cara import loop, actualizar_estado


from dotenv import load_dotenv

load_dotenv()



# ======================

# CONFIG

# ======================


modo = "chat"



# ======================

# INTERNET

# ======================


def hay_internet():

    try:

        socket.create_connection(("8.8.8.8", 53), timeout=2)

        return True

    except:

        return False



# ======================

# IA

# ======================


def obtener_respuesta(comando):

    try:

        if hay_internet():

            return responder_gemini(comando)  # ONLINE

        else:

            return responder_offline(comando)  # LOCAL

    except Exception as e:
        print ("Error online, usando offline:", e)
        return responder_offline(comando)



# ======================

# CEREBRO (hilo)

# ======================


def cerebro():

    global modo


    if USAR_TTS:

        hablar("Atlas en linea.")


    while True:


        actualizar_estado("idle")


        # ======================

        # MODO VOZ

        # ======================

        if modo == "voz":

            print("Escuchando wake word...")

            actualizar_estado("escuchando")


            texto = escuchar()


            if not texto:

                continue


            texto = texto.lower().strip()


            if WAKE_WORD in texto:

                print("ATLAS activado")


                if USAR_TTS:

                    hablar("Te escucho")


                actualizar_estado("escuchando")

                comando = escuchar()

            else:

                continue


        # ======================

        # MODO TEXTO / CHAT

        # ======================

        else:

            comando = input("Tu: ")


        if not comando:

            continue


        comando = comando.strip().lower()


        # ======================

        # SALIR

        # ======================

        if comando == "/salir":

            print("Apagando ATLAS")

            break


        # ======================

        # MODOS

        # ======================

        if comando.startswith("/modo"):

            if "voz" in comando:

                modo = "voz"

                print("Modo voz activado")

            elif "texto" in comando:

                modo = "texto"

                print("Modo texto activado")

            elif "chat" in comando:

                modo = "chat"

                print("Modo chat activado")

            continue


        # ======================

        # VISION

        # ======================

        if USAR_CAMARA:

            if hay_persona():

                print("Persona detectada")

            else:

                print("Nadie enfrente")


        # ======================

        # IA

        # ======================

        actualizar_estado("pensando")


        respuesta = obtener_respuesta(comando)


        print("ATLAS:", respuesta)


        actualizar_estado("hablando")


        # ======================

        # TTS

        # ======================

        if USAR_TTS and modo in ["voz", "texto"]:

            hablar(respuesta)


        actualizar_estado("idle")



# ======================

# MAIN

# ======================


def main():

    print("ATLAS iniciado")


    #  hilo del cerebro

    hilo = threading.Thread(target=cerebro, daemon=True)

    hilo.start()


    # pygame SIEMPRE en main thread

    loop()



if __name__ == "__main__":

    main()

