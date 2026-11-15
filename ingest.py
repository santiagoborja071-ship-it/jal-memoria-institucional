import os
import sqlite3
import pdfplumber
import docx

def leer_pdf(ruta):
    texto = ""
    with pdfplumber.open(ruta) as pdf:
        for pagina in pdf.pages:
            texto += (pagina.extract_text() or "") + "\n"
    return texto

def leer_word(ruta):
    doc = docx.Document(ruta)
    return "\n".join([parrafo.text for parrafo in doc.paragraphs])

def dividir_en_fragmentos(texto, tamano=500):
    return [texto[i:i+tamano] for i in range(0, len(texto), tamano) if texto[i:i+tamano].strip()]

def procesar_documentos():
    conexion = sqlite3.connect("conocimiento.db")
    cursor = conexion.cursor()
    carpeta = "documentos"

    for nombre_archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, nombre_archivo)
        texto_completo = ""

        if nombre_archivo.endswith(".pdf"):
            texto_completo = leer_pdf(ruta)
        elif nombre_archivo.endswith(".docx"):
            texto_completo = leer_word(ruta)
        else:
            continue

        fragmentos = dividir_en_fragmentos(texto_completo)
        for frag in fragmentos:
            cursor.execute(
                "INSERT INTO fragmentos (archivo, texto) VALUES (?, ?)",
                (nombre_archivo, frag)
            )
        print(f"Guardados {len(fragmentos)} fragmentos de {nombre_archivo}")

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    procesar_documentos()