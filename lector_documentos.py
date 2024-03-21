'''
Para leer documentos de texto y PDF en Python, puedes usar las bibliotecas docx y PyPDF2 respectivamente. 
Aquí tienes un ejemplo de cómo podrías hacerlo:

Primero, instala las bibliotecas necesarias con pip:

pip install python-docx PyPDF2


En este código, leer_documento lee un documento de Word y leer_pdf lee un PDF. Ambas funciones devuelven el
texto del documento como una cadena.
Por favor, asegúrate de reemplazar 'documento.docx' y 'documento.pdf' con las rutas a tus archivos.
'''

import docx
from PyPDF2 import PdfFileReader
'''
def leer_documento(doc_path):
  doc = docx.Document(doc_path)
  texto = [p.text for p in doc.paragraphs]
  return '\n'.join(texto)'''

def leer_pdf(pdf_path):
  with open(pdf_path, 'rb') as file:
    pdf = PdfFileReader(file)
    texto = [pdf.getPage(i).extractText() for i in range(pdf.getNumPages())]
  return '\n'.join(texto)
'''
# Uso de las funciones
texto_doc = leer_documento('documento.docx')
print(texto_doc)'''

texto_pdf = leer_pdf('presentación_entorno_de_ejecución.pdf')
print(texto_pdf)

with open('/m3_python_basico/presentación_entorno_de_ejecución.pdf', 'rb') as file: contenido = file.read()   # Code inside the 'with' block goes here