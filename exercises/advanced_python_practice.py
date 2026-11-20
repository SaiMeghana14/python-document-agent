# reference
list1 = [10, 20, 30]

list2 = list1

print(list1)
print(list2)

list1.append(40)

print(list1)
print(list2)

print(list1 is list2)

# Mutability
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

name = "Meghana"

name = name + " Python"

print(name)

# using .copy()
list1 = [10, 20, 30]

list2 = list1.copy()

list2.append(40)

print(list1)
print(list2)

# shallow copy
original = [[10, 20], [30, 40]]

copied = original.copy()

copied[0].append(50)

print(original)
print(copied)

# deep copy
import copy

original = [[10, 20], [30, 40]]

copied = copy.deepcopy(original)

copied[0].append(50)

print(original)
print(copied)

# Python Collections
# 1. List of documents

documents = [
    "report.pdf",
    "notes.txt",
    "invoice.csv",
    "policy.pdf"
]

print("Documents:")
for document in documents:
    print(document)

print("\nTotal documents:", len(documents))


# 2. Dictionary of document details

document = {
    "name": "report.pdf",
    "type": "PDF",
    "size": "2 MB",
    "status": "Imported"
}

print("\nDocument Details:")

print("Name:", document["name"])
print("Type:", document["type"])
print("Size:", document["size"])
print("Status:", document["status"])

# 3. Tuple of supported document formats

supported_formats = (".pdf", ".txt", ".md", ".csv")
supported_formats[0] = ".docx"
print("\nSupported Document Formats:")

for file_format in supported_formats:
    print(file_format)

print("Total supported formats:", len(supported_formats))

# 4. Set of document names

document_names = {
    "report.pdf",
    "notes.txt",
    "report.pdf",
    "invoice.csv"
}

print("\nUnique Document Names:")

for name in document_names:
    print(name)

print("Total unique documents:", len(document_names))

document_names.add("employee.pdf")

print("\nAfter adding a document:")
print(document_names)

document_names.add("notes.txt")

print("\nAfter adding a duplicate:")
print(document_names)

# Functions and Scope

# Parameters and Return Values

def get_document_info(filename):
    return "Processing document: " + filename

result = get_document_info("meeting_notes.md")

print("\n" + result)

# Step 2: Positional Arguments

def display_document(filename, file_type):
    print("Document Name:", filename)
    print("File Type:", file_type)


display_document("meeting_notes.md", "Markdown")

# Positional Arguments

def display_document(filename, file_type):
    print("Document Name:", filename)
    print("File Type:", file_type)


display_document("meeting_notes.md", "Markdown")
display_document("invoice.csv", "CSV")

# Keyword Arguments

def display_document(filename, file_type, status):
    print("Document Name:", filename)
    print("File Type:", file_type)
    print("Status:", status)

display_document(
    filename="invoice.csv",
    status="Processed",
    file_type="CSV"
)

# *args

def display_documents(*filenames):
    print("\nDocuments received:")

    for filename in filenames:
        print(filename)

display_documents(
    "report.pdf",
    "meeting_notes.md",
    "invoice.csv"
)
display_documents(
    "report.pdf",
    "meeting_notes.md",
    "invoice.csv",
    "employee_handbook.pdf"
)

# **kwargs

def display_document_details(**details):
    print("\nDocument Details:")

    for key, value in details.items():
        print(key, ":", value)


display_document_details(
    name="report.pdf",
    file_type="PDF",
    size="2 MB",
    status="Imported"
)
display_document_details(
    name="invoice.csv",
    file_type="CSV",
    status="Processed",
    pages=5,
    owner="Meghana"
)

# Step 6: Local and Global Scope

# Global variable
application_name = "Document Agent"


def process_document():
    # Local variable
    filename = "report.pdf"

    print("\nApplication:", application_name)
    print("Processing:", filename)


process_document()

print("Application Name:", application_name)
print(filename)

# Closures

def create_document_processor(filename):

    def process():
        print("Processing document:", filename)

    return process

processor = create_document_processor("meeting_notes.md")
processor()

second_processor = create_document_processor("invoice.csv")
second_processor()

# Mutable Default Arguments

def add_document(filename, documents=None):

    if documents is None:
        documents = []

    documents.append(filename)
    return documents

first_result = add_document("report.pdf")
second_result = add_document("invoice.csv")

print("First result:", first_result)
print("Second result:", second_result)

my_documents = ["meeting_notes.md"]

result = add_document("report.pdf", my_documents)

print("Updated documents:", result)

