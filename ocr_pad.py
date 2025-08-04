import pytesseract
from pdf2image import convert_from_path
from pathlib import Path
from tqdm import tqdm

# Si Tesseract no está en el PATH, descomenta la línea siguiente
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

PDF_PATH   = Path("entrada.pdf")       # <-- tu PDF
OUT_TXT    = Path("salida.txt")
TMP_FOLDER = Path("tmp_imgs")
TMP_FOLDER.mkdir(exist_ok=True)

# 1) Convertir cada página a imagen (dpi 300 = buena calidad)
print("Convirtiendo PDF a imágenes…")
images = convert_from_path(PDF_PATH, dpi=300, output_folder=TMP_FOLDER, fmt="png")

# 2) Pasar OCR página a página
print("Ejecutando OCR…")
all_text = []
for i, img in enumerate(tqdm(images, desc="Páginas")):
    text = pytesseract.image_to_string(img, lang="spa+eng")  # ajusta idiomas
    all_text.append(f"---------- Página {i+1} ----------\n{text}\n")

# 3) Guardar resultado
OUT_TXT.write_text("\n".join(all_text), encoding="utf-8")
print(f"Texto extraído en {OUT_TXT.resolve()}")

# 4) Limpieza opcional
# import shutil; shutil.rmtree(TMP_FOLDER)
