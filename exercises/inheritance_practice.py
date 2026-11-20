# Single inheritace
class Document:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Document name:", self.name)

class PDFDocument(Document):

    def show_format(self):
        print("Format: PDF")

pdf1 = PDFDocument("invoice.pdf")

pdf1.display()
pdf1.show_format()

# Multiple Inheritance
class Document:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Document name:", self.name)

class TextDocument(Document):

    def read_text(self):
        print("Reading text document")


class MarkdownDocument(TextDocument):

    def show_format(self):
        print("Format: Markdown")

    def show_description(self):
        print("This is a Markdown document")


md1 = MarkdownDocument("meeting_notes.md")

md1.display()
md1.read_text()
md1.show_format()
md1.show_description()

# Hierarchical Inheritance
class Document:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Document name:", self.name)

class PDFDocument(Document):

    def read_pdf(self):
        print("Reading PDF file")

class TextDocument(Document):

    def read_text(self):
        print("Reading text file")

class CSVDocument(Document):

    def read_csv(self):
        print("Reading CSV file")

pdf = PDFDocument("invoice.pdf")
text = TextDocument("notes.txt")
csv = CSVDocument("expenses.csv")

pdf.display()
pdf.read_pdf()

text.display()
text.read_text()

csv.display()
csv.read_csv()

# Multiple Inheritance
class DocumentReader:

    def read_document(self):
        print("Reading document")


class DocumentValidator:

    def validate_document(self):
        print("Validating document")


class DocumentProcessor(DocumentReader, DocumentValidator):

    def process_document(self):
        print("Processing document")


doc = DocumentProcessor()

doc.read_document()
doc.validate_document()
doc.process_document()

print(DocumentProcessor.mro())

# Hybrid Inheritance
class Document:

    def display(self):
        print("This is a document")


class PDFDocument(Document):

    def read_pdf(self):
        print("Reading PDF")


class TextDocument(Document):

    def read_text(self):
        print("Reading text")


class DocumentProcessor(PDFDocument, TextDocument):

    def process(self):
        print("Processing document")

doc = DocumentProcessor()

doc.display()
doc.read_pdf()
doc.read_text()
doc.process()

print(DocumentProcessor.mro())

# Method overriding
class Document:

    def display(self):
        print("Displaying a document")

class PDFDocument(Document):

    def display(self):
        print("Displaying a PDF document")

doc = PDFDocument()

doc.display()

# using super()
class Document:

    def display(self):
        print("Displaying a document")

class PDFDocument(Document):

    def display(self):
        super().display()
        print("Additional PDF information")

doc = PDFDocument()
doc.display()

# Using super() with __init__()
class Document:

    def __init__(self, name):
        self.name = name

class PDFDocument(Document):

    def __init__(self, name, page_count):
        super().__init__(name)
        self.page_count = page_count

pdf = PDFDocument("invoice.pdf", 5)

print(pdf.name)
print(pdf.page_count)

# isinstance()
class Document:
    pass


class PDFDocument(Document):
    pass


pdf = PDFDocument()

print(isinstance(pdf, PDFDocument))
print(isinstance(pdf, Document))
print(isinstance(pdf, str))"""

# issubclass()
class Document:
    pass


class PDFDocument(Document):
    pass


class TextDocument(Document):
    pass


print(issubclass(PDFDocument, Document))
print(issubclass(TextDocument, Document))
print(issubclass(Document, PDFDocument))

# Polymorphism
class PDFDocument:

    def read(self):
        print("Reading PDF document")


class TextDocument:

    def read(self):
        print("Reading text document")


class CSVDocument:

    def read(self):
        print("Reading CSV document")


documents = [
    PDFDocument(),
    TextDocument(),
    CSVDocument()
]

for document in documents:
    document.read()

# Duck typing
class PDFReader:

    def read(self):
        print("Reading PDF file")

class CSVReader:

    def read(self):
        print("Reading CSV file")

def process_document(reader):
    reader.read()

pdf = PDFReader()
csv = CSVReader()

process_document(pdf)
process_document(csv)

# Abstract classes
from abc import ABC, abstractmethod


class DocumentReader(ABC):

    @abstractmethod
    def read(self):
        pass


class PDFReader(DocumentReader):

    def read(self):
        print("Reading PDF file")


class CSVReader(DocumentReader):

    def read(self):
        print("Reading CSV file")


pdf = PDFReader()
csv = CSVReader()

pdf.read()
csv.read()

# Protocols
from typing import Protocol


class Reader(Protocol):

    def read(self) -> None:
        ...


class PDFReader:

    def read(self) -> None:
        print("Reading PDF")


class CSVReader:

    def read(self) -> None:
        print("Reading CSV")


def process_document(reader: Reader):
    reader.read()


process_document(PDFReader())
process_document(CSVReader())

# Composition
class PDFReader:

    def read(self, file_name):
        print("Reading PDF:", file_name)

class CSVReader:

    def read(self, file_name):
        print("Reading CSV:", file_name)

class DocumentProcessor:

    def __init__(self, reader):
        self.reader = reader

    def process(self, file_name):
        self.reader.read(file_name)


pdf_reader = PDFReader()

processor = DocumentProcessor(pdf_reader)

processor.process("invoice.pdf")

csv_reader = CSVReader()

processor = DocumentProcessor(csv_reader)

processor.process("expenses.csv")