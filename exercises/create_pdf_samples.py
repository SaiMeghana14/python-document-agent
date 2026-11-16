from pathlib import Path

from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas

output_folder = Path("samples/input")
output_folder.mkdir(parents=True, exist_ok=True)

# Create a PDF containing selectable text.
text_pdf = output_folder / "text_sample.pdf"
pdf = canvas.Canvas(str(text_pdf))
pdf.drawString(72, 750, "PDF Text Extraction Test")
pdf.drawString(72, 720, "This text should be extractable.")
pdf.save()

# Create an image to place inside a PDF.
image_path = output_folder / "sample_image.png"
image = Image.new("RGB", (500, 200), "white")
draw = ImageDraw.Draw(image)
draw.text((30, 80), "Image-only PDF test", fill="black")
image.save(image_path)

# Create a PDF containing only the image.
image_pdf = output_folder / "image_only_sample.pdf"
pdf = canvas.Canvas(str(image_pdf))
pdf.drawImage(str(image_path), 72, 650, width=400, height=160)
pdf.save()

print("Created both PDF test files.")
