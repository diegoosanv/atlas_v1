from google import genai

import os

from dotenv import load_dotenv


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def responder_gemini(texto):

    try:

        response = client.models.generate_content(

            model="gemini-2.0-flash",

            contents=texto

        )

        return response.text

    except Exception as e:

        return f"Error Gemini: {e}"

