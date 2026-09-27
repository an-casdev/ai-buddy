import pyautogui
import io
import base64
from google import genai

client = genai.Client(api_key="GEMINI_API")

def capturar_pantalla():
    screenshot = pyautogui.screenshot()
    # Reducir tamaño a la mitad para no saturar el servidor
    width, height = screenshot.size
    screenshot = screenshot.resize((width//2, height//2))
    buffer = io.BytesIO()
    screenshot.save(buffer, format="JPEG", quality=70)  # JPEG más liviano que PNG
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def preguntar_con_pantalla(pregunta):
    imagen = capturar_pantalla()
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[{
            "parts": [
                {"inline_data": {"mime_type": "image/JPEG", "data": imagen}},
                {"text": f"Eres un asistente que ve la pantalla del usuario y le ayuda con lo que está haciendo. Responde de forma concisa y útil: {pregunta}"}
            ]
        }]
    )
    return response.text

# LOOP INTERACTIVO
print("👁️ AI Buddy activo — ve tu pantalla en tiempo real")
print("Escribe 'salir' para terminar\n")

while True:
    pregunta = input("Tú: ")
    if pregunta.lower() == "salir":
        print("AI Buddy: ¡Hasta luego! 👋")
        break
    respuesta = preguntar_con_pantalla(pregunta)
    print(f"\nAI Buddy: {respuesta}\n")