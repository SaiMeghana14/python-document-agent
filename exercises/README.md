# Python Exercises Guide

This folder contains individual Python programs created while completing the Python Foundations and Document Tools assignment.

Each program focuses on a particular Python concept. Run the commands from the project root folder:

```powershell
uv run python exercises/FILE_NAME.py
```

Replace `FILE_NAME.py` with the exercise file you want to run.

## 1. Exercise list

| Exercise file | Concepts covered | Command |
|---|---|---|
| `calculator.py` | Functions, conditions, parameters and return values | `uv run python exercises/calculator.py` |
| `file_tools.py` | pathlib, JSON, regular expressions, dates and Decimal | `uv run python exercises/file_tools.py` |
| `import_example.py` | Imports, modules and the main guard | `uv run python exercises/import_example.py` |
| `imports_and_context.py` | Generators, CSV reading and context managers | `uv run python exercises/imports_and_context.py` |
| `interpreter_info.py` | Python interpreter and virtual environment information | `uv run python exercises/interpreter_info.py` |
| `logging_demo.py` | Logging levels, exceptions and tracebacks | `uv run python exercises/logging_demo.py` |
| `lookup_benchmark.py` | Searching in lists, sets and dictionaries | `uv run python exercises/lookup_benchmark.py` |
| `python_fundamentals.py` | Mutable objects, copying, closures, classes, dataclasses and decorators | `uv run python exercises/python_fundamentals.py` |
| `storage_example.py` | File storage and pathlib operations | `uv run python exercises/storage_example.py` |
| `data_tools.py` | pandas, CSV cleaning, Decimal, joins and NumPy | `uv run python exercises/data_tools.py` |
| `create_pdf_samples.py` | Creating sample PDF documents for testing | `uv run python exercises/create_pdf_samples.py` |
| `debugger_practice.py` | Debugging, breakpoints and inspecting variables | `uv run python exercises/debugger_practice.py` |

## 2. Important concepts learned

### Python fundamentals

- Functions help divide a program into smaller reusable parts.
- Lists, dictionaries and sets store collections of values.
- Mutable objects can be changed after creation.
- A shallow copy shares nested objects, while a deep copy creates independent nested copies.
- Classes and dataclasses help organise related data and behaviour.
- Instance methods work with object data; class methods work with the class; static methods are utility functions associated with a class.
- Decorators can add behaviour to functions.

### Modules and imports

- Modules allow code to be organised across multiple Python files.
- Imports make functions and classes available in other modules.
- The `if __name__ == "__main__":` guard prevents script-only code from running when a module is imported.
- Circular imports happen when modules depend on each other in a way that creates an import cycle.
- Naming a file after a standard-library module can cause module-shadowing problems.

### File handling

- `pathlib` provides convenient ways to work with file paths.
- JSON can store structured information.
- CSV files can be read and processed using Python's CSV module or pandas.
- Context managers help manage resources such as open files.
- Generators produce values one at a time instead of creating an entire collection at once.

### Data processing

- pandas is useful for cleaning and analysing tabular data.
- Missing values need to be handled carefully.
- Employee IDs should be treated as text when leading zeros are important.
- `Decimal` is useful when accurate decimal arithmetic is required, especially for money.
- Joins combine data from different tables. Duplicate keys can cause unexpected row multiplication.
- NumPy arrays have shapes and data types, and broadcasting allows compatible arrays to work together.

### Logging and debugging

- Logging records application events at different levels.
- INFO messages describe normal application activity.
- WARNING messages indicate something unexpected that does not necessarily stop execution.
- ERROR messages report failures.
- A debugger allows a program to be paused and inspected.
- Variables can be inspected while stepping through code to understand where a problem occurs.

## 3. What to observe when running exercises

| Exercise | What to observe |
|---|---|
| `python_fundamentals.py` | A new list is created for a later function call. Compare how shallow and deep copies behave with nested lists. |
| `imports_and_context.py` | Observe how the generator yields rows one at a time and how the context manager handles the file. |
| `data_tools.py` | The original CSV remains unchanged. The cleaned output removes the duplicate row, preserves leading zeros in employee IDs and keeps missing values. |
| `lookup_benchmark.py` | Compare list, set and dictionary lookup times for different collection sizes. The exact timings depend on the computer. |
| `logging_demo.py` | Observe INFO and WARNING messages and the traceback displayed by the error example. |
| `debugger_practice.py` | Use the debugger to inspect variables and identify the incorrect calculation. |

## 4. Running the data exercise

```powershell
uv run python exercises/data_tools.py
```

The exercise reads the sample expenses CSV and demonstrates data cleaning and analysis.

The cleaned CSV is saved separately under `data/`. The original sample file is not overwritten.

## 5. Running the logging exercise

```powershell
uv run python exercises/logging_demo.py
```

This demonstrates logging messages at different levels and how an exception traceback can be recorded.

The logging test can be run separately:

```powershell
uv run python -m pytest tests/test_logging.py -v
```

## 6. Running the debugger exercise

```powershell
uv run python exercises/debugger_practice.py
```

The exercise contains an intentional calculation mistake. During the debugging practice, a breakpoint was used to pause execution and inspect variables.

The breakpoint was removed after the debugging exercise so that Ruff would not report a leftover debugging statement.

## 7. Recording exercise observations

After running each exercise, record:

1. The command used.
2. The important output you observed.
3. The concept demonstrated.
4. Any issue you encountered and how you resolved it.

Use your actual output and experience. Benchmark timings may differ between computers, so do not copy timings as fixed expected results.
