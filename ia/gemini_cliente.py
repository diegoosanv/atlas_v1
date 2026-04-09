import os

from dotenv import load_dotenv

from google import genai


from memoria.historial import contexto

from memoria.recuerdos import obtener


load_dotenv()


def responder_gemini(texto):

    try:

        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


        ctx = contexto()

        recuerdos = obtener()


        prompt = f"""

Eres ATLAS, un asistente inteligente.


Datos del usuario:

{recuerdos}


Contexto:

{ctx}


Usuario: {texto}

ATLAS:

"""


        response = client.models.generate_content(

            model="gemini-2.0-flash",

            contents=prompt

        )


        return response.text


    except Exception as e:

        return f"Error Gemini: {e}"
