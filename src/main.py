import json
import os
import speech_recognition as sr
import keyboard
import asyncio

# Obtener el directorio donde se encuentra el script actual
current_directory = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(current_directory, 'config.json')

# Leer el archivo de configuración
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)
    language = config['language']
    activation_key_code = config['activation_key']['code']
    activation_key_name = config['activation_key']['name']
    exit_key_code = config['exit_key']['code']
    exit_key_name = config['exit_key']['name']


# Flags para controlar el estado de escucha y salida del programa
is_listening = False
exit_program = False


def on_key_press(event):
    global is_listening, exit_program
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == activation_key_code:
            is_listening = not is_listening  # Cambiar el estado de is_listening
        elif event.name == exit_key_code:
            exit_program = True  # Establecer flag para salir del programa

async def listen():
    """Comienza y detiene la escucha con la presión de la tecla de activación y sale con la tecla de salida."""
    global is_listening, exit_program
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while not exit_program:
            print(f"Presiona la tecla {activation_key_name} para comenzar a hablar.")
            while not is_listening and not exit_program:
                await asyncio.sleep(0.1)  # Esperar hasta que se presione la tecla de activación

            if is_listening:
                print("Escuchando... Presiona la tecla de activación nuevamente para transcribir.")
                audio_data = []
                while is_listening and not exit_program:
                    try:
                        audio = recognizer.listen(source, timeout=1)
                        audio_data.append(audio)
                    except sr.WaitTimeoutError:
                        continue  # Continúa escuchando si no se detecta el audio

                if audio_data:
                    print("Transcribiendo...")
                    final_audio = sr.AudioData(b''.join([a.get_raw_data() for a in audio_data]), source.SAMPLE_RATE, source.SAMPLE_WIDTH)
                    try:
                        text = recognizer.recognize_google(final_audio, language=language)
                        print("Creo que dijiste: " + text)
                    except sr.UnknownValueError:
                        print("Lo siento, no pude entender el audio.")
                    except sr.RequestError as e:
                        print(f"Error en el servicio de Google; {e}")

    print("Finalizando el programa...")

# Configurar los hooks para las teclas
keyboard.on_press(on_key_press)

# Ejecutar la función listen de manera asíncrona y esperar a que termine
asyncio.run(listen())

# Limpieza antes de salir
keyboard.unhook(on_key_press)
