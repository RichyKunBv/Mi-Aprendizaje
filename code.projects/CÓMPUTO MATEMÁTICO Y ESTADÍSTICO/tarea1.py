# --- Generacion de requirements.txt (para mas comodidad y respaldo) ---
import subprocess

try:
    with open("requirements.txt", "w") as f:
        subprocess.run(["pip", "freeze"], stdout=f, check=True)
except Exception as e:
    print(f"No se pudo generar el archivo requirements.txt: {e}")
# ----------------- De preferencia ignorelo profesor ------------------

# se importa la libreria numpy
import numpy as np

# libreria para generar PDF (se genera un archivo TXT y luego se convierte a PDF)
from fpdf import FPDF, XPos, YPos

# variable con datos
datos = [1, 2, 3, 4, 5]

#calculo de media
media = np.mean(datos)

# calculo de varianza
varianza = np.var(datos)

# se imprimen los resultados en la terminal
print(f"media: {media}")
print(f"varianza: {varianza}")

# referencias (tambien impresas en la terminal)
print("Referencias:\n"
    "- Conocimientos basicos de Python aprendidos en la carrera por el profesor Pedro\n"
    "- Documentacion oficial de Numpy: https://numpy.org/doc/stable/\n"
    "- Documentacion oficial de FPDF: https://pyfpdf.github.io/fpdf2/\n"
    "- Documentacion oficial de Numpy.var: https://numpy.org/doc/stable/reference/generated/numpy.var.html")


# se crea un TXT con todos los resultados obternidos
with open("resultados1.txt", "w") as f:
    f.write("Resultados de la Tarea 1\n")
    f.write(f"Datos: {datos}\n")
    f.write(f"Resultados Calculados:\n")
    f.write(f"media: {media}\n")
    f.write(f"varianza: {varianza}\n\n")
    f.write("Referencias:\n")
    f.write("-Conocimientos basicos de Python aprendidos en la carrera por el profesor Pedro\n")
    f.write("-Documentacion oficial de Numpy: https://numpy.org/doc/stable/\n")
    f.write("-Documentacion oficial de FPDF: https://pyfpdf.github.io/fpdf2/\n")
    f.write("-Documentaion oficial de Numpy.var: https://numpy.org/doc/stable/reference/generated/numpy.var.html\n")

# Generación del PDF a partir del TXT creado
try:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    # Leer el txt y escribirlo en el PDF
    with open("resultados1.txt", "r") as f:
        for linea in f:
            pdf.cell(200, 10, text=linea.encode('latin-1', 'replace').decode('latin-1'), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

    pdf.output("resultados1.pdf")

    print("\n[INFO] El PDF ha sido generado exitosamente desde el archivo de texto.")
except Exception as e:
    print(f"[ERROR] No se pudo generar el PDF: {e}")