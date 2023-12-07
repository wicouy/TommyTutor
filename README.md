# Asistente de Voz en Python

Este proyecto es un asistente de voz desarrollado en Python, que utiliza reconocimiento de voz para realizar tareas simples. El asistente puede ser activado y desactivado con una tecla específica y está configurado para ser altamente personalizable a través de un archivo de configuración.

## Características

- Reconocimiento de voz en varios idiomas.
- Activación/desactivación mediante tecla personalizable.
- Finalización del programa con tecla específica.
- Configuración sencilla a través de un archivo JSON.

## Requisitos

Para ejecutar este asistente de voz, necesitarás Python instalado en tu sistema, así como las siguientes bibliotecas:

- `speech_recognition`
- `keyboard`
- `asyncio`

Puedes instalar estas dependencias usando `pip`:
pip install SpeechRecognition keyboard asyncio


## Configuración del Asistente de Voz

El asistente utiliza un archivo `config.json` para personalizar su comportamiento. Este archivo debe ubicarse en el mismo directorio que el script principal (`main.py`). Los siguientes son los parámetros que puedes configurar:

### Estructura del Archivo `config.json`

{
    "language": "es-ES",
    "activation_key": {
        "code": "space",
        "name": "Espaciadora"
    },
    "exit_key": {
        "code": "esc",
        "name": "Escape"
    }
}



## Parámetros

- `language`: Define el idioma para el reconocimiento de voz. Utiliza códigos de idioma compatibles con la API de Google Speech Recognition, como `es-ES` para español, `en-US` para inglés, etc.
- `activation_key`: Tecla para activar/desactivar la escucha. Debe ser un nombre de tecla reconocido por la biblioteca `keyboard`, como `space` para la barra espaciadora.
- `exit_key`: Tecla para terminar la ejecución del programa. Similar a `activation_key`, usa un nombre de tecla reconocido por `keyboard`.

## Uso

Para usar el asistente de voz, ejecuta el script `main.py`. Presiona la tecla de activación para comenzar a hablar y vuelve a presionarla para que el asistente procese y transcriba tu voz. Si deseas salir del programa, presiona la tecla de salida.
