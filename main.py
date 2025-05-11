import PyPDF2
import pyttsx3

# Ruta del archivo PDF
ruta_pdf = 'fund-IE00B42W4L06-x-ray.pdf'

# Inicializar el motor de texto a voz
motor = pyttsx3.init()

# Abrir el archivo PDF
with open(ruta_pdf, 'rb') as archivo:
    lector = PyPDF2.PdfReader(archivo)
    texto = ""
    for pagina in lector.pages:
        texto += pagina.extract_text()

# Leer el texto en voz alta
motor.say(texto)
motor.runAndWait()

# Guardar el archivo de audio
# motor.save_to_file(texto, 'salida_audio.mp3')
# motor.runAndWait()
