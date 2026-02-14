import subprocess


def responder_offline(texto):

    """

    Envía un prompt a Ollama y devuelve la respuesta

    """

    prompt = f"""

Eres ATLAS, un asistente virtual privado.

Responde SIEMPRE en español.

Usuario dice: {texto}

ATLAS:

"""


    try:

        resultado = subprocess.run(

            ["ollama", "run", "phi3"],

            input=prompt,

            text=True,

            capture_output=True

        )

        return resultado.stdout.strip()

    except Exception as e:

        return f"Error con Ollama: {e}"
