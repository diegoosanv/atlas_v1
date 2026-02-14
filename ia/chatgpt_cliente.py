import os

from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def responder_online(texto):

    """

    Envía el mensaje a ChatGPT (online)

    """

    try:

        respuesta = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[

                {

                    "role": "system",

                    "content": (

                        "Eres ATLAS, un asistente virtual privado. "

                        "Hablas SIEMPRE en español. "

                        "Eres claro, respetuoso y directo."

                    )

                },

                {"role": "user", "content": texto}

            ]

        )

        return respuesta.choices[0].message.content.strip()


    except Exception as e:

        return f"Error con ChatGPT: {e}"
