# OCR de PDFs escaneados en Python

Convierte un PDF compuesto por imágenes a texto utilizando Poppler + Tesseract.

## Requisitos

| Software | Windows | macOS | Linux |
|----------|---------|-------|-------|
| **Python ≥ 3.9** | https://python.org/downloads | Homebrew / pkg | repo |
| **Tesseract OCR** | `winget install tesseract` | `brew install tesseract` | `sudo apt install tesseract-ocr` |
| **Poppler** | `winget install oschwartz.poppler` | `brew install poppler` | `sudo apt install poppler-utils` |

> En Windows puedes usar **Chocolatey** en vez de Winget (`choco install poppler tesseract`).

## Instalación

```bash
git clone https://github.com/tu-usuario/ocr-pdf-ocr.git
cd ocr-pdf-ocr

python -m venv .venv
source .venv/Scripts/activate      # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt


USO: 
Coloca tu archivo pdf cambiale el nombre a: entrada.pdf en la carpeta donde está el cor_pad.py 

Ejecuta en la consola: python ocr_pdf.py para correr el programa.

El texto aparecerá en salida.txt

Consideraciones:
Si Poppler o Tesseract no están en el PATH, edita ocr_pdf.py y fija poppler_path o pytesseract.tesseract_cmd.

