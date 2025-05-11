import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import pyttsx3
import os
import threading


def seleccionar_pdf():
    archivo_pdf = filedialog.askopenfilename(
        filetypes=[("Archivos PDF", "*.pdf")],
        title="Selecciona un archivo PDF"
    )
    if archivo_pdf:
        threading.Thread(target=convertir_a_audio, args=(archivo_pdf,), daemon=True).start()


def convertir_a_audio(ruta_pdf):
    try:
        with open(ruta_pdf, 'rb') as archivo:
            lector = PyPDF2.PdfReader(archivo)
            texto = ""
            for pagina in lector.pages:
                texto += pagina.extract_text()

        if not texto.strip():
            messagebox.showwarning("Texto vacío", "No se pudo extraer texto del PDF.")
            return

        nombre_base = os.path.splitext(os.path.basename(ruta_pdf))[0]
        salida_audio = f"{nombre_base}.wav"

        # Crear el motor dentro del hilo y destruirlo después
        motor = pyttsx3.init()
        motor.save_to_file(texto, salida_audio)
        motor.runAndWait()
        motor.stop()
        del motor

        messagebox.showinfo("Éxito", f"Audio guardado como: {salida_audio}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")



ventana = tk.Tk()
ventana.title("PDF a Audio")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Selecciona un PDF para convertir a audio")
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Seleccionar PDF", command=seleccionar_pdf)
boton.pack(pady=10)

ventana.mainloop()





