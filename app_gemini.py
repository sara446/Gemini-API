import os
from google import genai
from dotenv import load_dotenv


# 1. Cargar variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")


# 2. Inicializar el cliente de Gemini
client = genai.Client(api_key=clave_api)


def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")

    if not clave_api:
        print("❌ Error: No se encontró la variable de entorno GEMINI_API_KEY")
        return

    try:
        # 3. Llamada al modelo
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=(
                "Me gustó mucho la clase porque es muy interactiva; "
                "sin embargo, tuvimos problemas con el internet."
                
            ),
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")


if __name__ == "__main__":
    ejecutar_consulta()
