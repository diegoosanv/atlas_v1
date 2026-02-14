from voz.stt import escuchar

from voz.tts import hablar

from vision.rostros import hay_persona

from ia.ollama_cliente import responder_offline

from ia.chatgpt_cliente import responder_online

from config import WAKE_WORD, USAR_CAMARA, USAR_TTS


import socket


# Modos disponibles:

# chat   -> texto normal

# texto  -> escribes, ATLAS habla

# voz    -> wake word + voz

modo = "chat"



def hay_internet():

    try:

        socket.create_connection(("8.8.8.8", 53), timeout=2)

        return True

    except:

        return False



def obtener_respuesta(comando):

    if hay_internet():

        return responder_online(comando)

    else:

        return responder_offline(comando)



def main():

    global modo


    print("ATLAS iniciado")


    if USAR_TTS:

        hablar("Atlas en linea.")


    while True:


        # ======================

        # MODO VOZ

        # ======================

        if modo == "voz":

            print("Escuchando wake word...")

            texto = escuchar()


            if not texto:

                continue


            texto = texto.lower().strip()


            if WAKE_WORD in texto:

                print("ATLAS activado")


                if USAR_TTS:

                    hablar("Te escucho")


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

        # COMANDOS DE SISTEMA

        # ======================

        if comando.startswith("/modo"):

            if "voz" in comando:

                modo = "voz"

                print("Modo voz activado")

            elif "texto" in comando:

                modo = "texto"

                print("Modo texto activado. ATLAS hablara.")

            elif "chat" in comando:

                modo = "chat"

                print("Modo chat activado")

            continue


        if comando == "/salir":

            print("Apagando ATLAS")

            break


        # ======================

        # VISION (opcional)

        # ======================

        if USAR_CAMARA:

            if hay_persona():

                print("Persona detectada")

            else:

                print("Nadie enfrente")


        # ======================

        # IA

        # ======================

        respuesta = obtener_respuesta(comando)


        print("ATLAS:", respuesta)


        # ======================

        # TTS si corresponde

        # ======================

        if USAR_TTS and modo in ["voz", "texto"]:

            hablar(respuesta)



if __name__ == "__main__":

    main()








