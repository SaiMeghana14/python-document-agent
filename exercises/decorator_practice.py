"""# Understanding function wrapping

def greeting():
    print("Hello! Welcome to Python.")

def wrapper_function():
    print("Before calling the function.")

    greeting()

    print("After calling the function.")

wrapper_function()

# Step 3: Creating a decorator

def my_decorator(func):

    def wrapper():
        print("Before function execution.")

        func()

        print("After function execution.")

    return wrapper

@my_decorator
def greeting():
    print("Hello! Welcome to Python.")

greeting()

# Step 4: Decorator with arguments

def my_decorator(func):

    def wrapper(*args, **kwargs):

        print("Function is starting.")

        func(*args, **kwargs)

        print("Function has finished.")

    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

@my_decorator
def add_numbers(a, b):
    print("Sum:", a + b)

greet("Meghana")
add_numbers(10, 20)

# Step 5: Timing decorator

import time


def measure_time(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print("Execution time:", execution_time, "seconds")

        return result

    return wrapper


@measure_time
def read_document():

    with open("exercises/sample.txt", "r") as file:
        content = file.read()

    print("Document content:", content)

    return content

read_document()

# Step 7: Understanding type hints

def add_numbers(a: int, b: int) -> int:

    result = a + b

    return result

answer = add_numbers(10, 20)
answer1 = add_numbers("Hello", "Python")

print("Sum:", answer)
print("Sum:", answer1)

# Step 9: Type hints with document functions

def get_document_info(filename: str, content: str) -> str:

    message = f"Document: {filename}, Content: {content}"

    return message


result = get_document_info("meeting_notes.txt", "Project discussion")

print(result)

# Step 11: Timing decorator with type hints

import time


def measure_time(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print("Execution time:", end_time - start_time, "seconds")

        return result

    return wrapper


@measure_time
def read_document(filename: str) -> str:

    with open(filename, "r") as file:
        content = file.read()

    return content


document = read_document("exercises/sample.txt")

print("Document content:", document)

# Task 4.9 - Reading CSV files

import csv

with open("exercises/employees.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)"""

# Writing CSV files

import csv

employees = [
    ["employee_id", "name", "department"],
    ["106", "Suresh", "IT"],
    ["107", "Anjali", "HR"],
]

with open("exercises/new_employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(employees)

print("CSV file created successfully.")





