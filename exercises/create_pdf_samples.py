"""Create local PDF boundary samples for testing the document importer."""

from pathlib import Path

from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas


def main() -> None:
    output_folder = Path("samples/input")
    output_folder.mkdir(parents=True, exist_ok=True)

    # The same simple text is placed in three PDFs with selectable text.
    for number in range(1, 4):
        pdf_path = output_folder / f"text_sample_{number}.pdf"
        pdf = canvas.Canvas(str(pdf_path))
        pdf.drawString(72, 750, f"Selectable PDF sample {number}")
        pdf.drawString(72, 720, "This text can be extracted by a PDF reader.")
        pdf.save()

    # Create an image and put it into a PDF. The PDF has no text layer.
    image_path = output_folder / "image_only_sample.png"
    image = Image.new("RGB", (500, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.text((30, 80), "Image-only PDF test", fill="black")
    image.save(image_path)

    pdf_path = output_folder / "image_only_sample.pdf"
    pdf = canvas.Canvas(str(pdf_path))
    pdf.drawImage(str(image_path), 72, 650, width=400, height=160)
    pdf.save()

    print("Created three text PDFs and one image-only PDF in", output_folder)
    print("The PNG is also available as an unsupported-image test case.")


if __name__ == "__main__":
    main()
