number = 10
result = number / 0
print(result)

# try and except
try:
    number = 10 / 0
    print(number)

except ZeroDivisionError:
    print("Cannot divide a number by zero.")

print("Program continues...")

# try, except, else and finally
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division successful!")
    print("Result:", number)

finally:
    print("Execution completed.")

# Using raise
def read_document(filename):

    if filename == "":
        raise ValueError("Filename cannot be empty.")

    print("Reading document:", filename)

try:
    read_document("meeting_notes.md")

except ValueError as error:
    print("Error:", error)

# Using raise ... from
def read_document_content(content):

    try:
        number = int(content)
        return number

    except ValueError as error:
        raise ValueError("Document content must contain a valid number.") from error

try:
    result = read_document_content("hello")
    print("Result:", result)

except ValueError as error:
    print("Error:", error)
    print("Original cause:", error.__cause__)

# Step 7: Reading files and handling exceptions

def read_file(filename):

    try:
        with open(filename, "r") as file:
            content = file.read().strip()

        number = int(content)
        print("Successfully read:", number)

    except FileNotFoundError:
        print("Error: File does not exist.")

    except ValueError:
        print("Error: File contains invalid data.")

    except OSError as error:
        print("File reading error:", error)

# Test 1: Existing file with valid data
read_file("exercises/sample.txt")

# Test 2: File that does not exist
read_file("exercises/missing.txt")

# Test 3: Existing file with invalid data
read_file("exercises/invalid_sample.txt")

# Step 8: Batch processing with exception handling

def process_document(filename):

    try:
        with open(filename, "r") as file:
            content = file.read().strip()

        number = int(content)
        print(filename, "processed successfully:", number)

    except FileNotFoundError:
        print(filename, "- File not found.")

    except ValueError:
        print(filename, "- Invalid document data.")

    except OSError as error:
        print(filename, "- File error:", error)

documents = [
    "exercises/sample.txt",
    "exercises/invalid_sample.txt",
    "exercises/sample.txt"
]

for document in documents:
    process_document(document)

print("Batch processing completed.")

# Context managers
file = open("exercises/sample.txt", "r")
content = file.read()
file.close()
# if error befor file.close(), file remains open
# Using a context manager

with open("exercises/sample.txt", "r") as file:
    content = file.read()

print(content)
print("File reading completed.")

# Step 3: File closing when an error occurs

try:
    with open("exercises/sample.txt", "r") as file:
        print("File opened successfully.")

        content = file.read()
        print(content)

        raise ValueError("Something went wrong!")

except ValueError as error:
    print("Error:", error)

print("Is the file closed?", file.closed)

# Step 5: First generator

def document_numbers():

    yield 101
    yield 102
    yield 103
    yield 104
    yield 105

for number in document_numbers():
    print("Document ID:", number)

# Step 6: Comparing return and yield

def normal_function():
    print("Normal function started")
    return 10
    print("This line will not execute")

def generator_function():
    print("Generator started")
    yield 10
    print("Generator resumed")
    yield 20

print("--- Normal Function ---")
result = normal_function()
print("Returned:", result)

print("--- Generator Function ---")
result = generator_function()

print("First value:", next(result))
print("Second value:", next(result))

# Step 7: Reading CSV rows using a generator

import csv

def read_employees(filename):

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row

for employee in read_employees("exercises/employees.csv"):
    print(employee)

# Step 8: Stopping generator processing early

import csv

def read_employees(filename):

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row

employees = read_employees("exercises/employees.csv")

print("First employee:", next(employees))
print("Second employee:", next(employees))

employees.close()

print("Generator closed.")





