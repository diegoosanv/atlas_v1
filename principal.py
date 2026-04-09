import socket

import time


from voz.stt import escuchar

from voz.tts import hablar

from vision.rostros import hay_persona


from ia.ollama_cliente import responder_offline

from ia.gemini_cliente import responder_gemini


from config import WAKE_WORD, USAR_CAMARA, USAR_TTS

from interfaz.cara import iniciar_cara, actualizar_estado, actualizar_pantalla



modo = "chat"



def hay_internet():

    try:

        socket.create_connection(("8.8.8.8", 53), timeout=2)

        return True

    except:

        return False



def obtener_respuesta(comando):

    if hay_internet():

        try:

            return responder_gemini(comando)

        except Exception as e:

            print("Error online:", e)

            return responder_offline(comando)

    else:

        return responder_offline(comando)



def main():

    global modo


    print("ATLAS iniciado")


    # iniciar pygame en hilo principal

    iniciar_cara()


    if USAR_TTS:

        hablar("Atlas en línea.")


    while True:


        #  actualizar pantalla SIEMPRE

        actualizar_pantalla()


        # ======================

        # INPUT

        # ======================

        actualizar_estado("escuchando")

        comando = input("Tu: ")


        if not comando:

            continue


        comando = comando.strip().lower()


        # ======================

        # COMANDOS

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


        if comando == "/salir":

            print("Apagando ATLAS")

            break


        # ======================

        # VISIÓN

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


        actualizar_estado("hablando")


        print("ATLAS:", respuesta)


        # ======================

        # TTS

        # ======================

        if USAR_TTS and modo in ["voz", "texto"]:

            hablar(respuesta)


        actualizar_estado("idle")


        # pequeño delay para estabilidad

        time.sleep(0.1)



if __name__ == "__main__":

    main()

