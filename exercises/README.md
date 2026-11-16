# Exercise guide

Run commands from the project root with `uv run python <file>`.

| Topic | File | Command |
|---|---|---|
| Functions, conditions and exceptions | `calculator.py` | `uv run python exercises/calculator.py` |
| File paths, JSON, regular expressions, dates and Decimal | `file_tools.py` | `uv run python exercises/file_tools.py` |
| Importing a module and a main guard | `import_example.py` | `uv run python exercises/import_example.py` |
| CSV generator and context manager | `imports_and_context.py` | `uv run python exercises/imports_and_context.py` |
| Interpreter and virtual environment | `interpreter_info.py` | `uv run python exercises/interpreter_info.py` |
| Logging levels and exception traceback | `logging_demo.py` | `uv run python exercises/logging_demo.py` |
| List, set and dictionary lookup | `lookup_benchmark.py` | `uv run python exercises/lookup_benchmark.py` |
| Copies, closures, dataclasses, methods and decorator | `python_fundamentals.py` | `uv run python exercises/python_fundamentals.py` |
| pathlib file size | `storage_example.py` | `uv run python exercises/storage_example.py` |
| pandas, CSV, Decimal, joins and NumPy | `data_tools.py` | `uv run python exercises/data_tools.py` |

## What to observe

- `python_fundamentals.py`: the second call to `add_item` starts with a new list; the shallow copy shares its nested list, while the deep copy does not.
- `imports_and_context.py`: rows are yielded one at a time and the file closes when iteration finishes.
- `data_tools.py`: the source CSV is not edited. The cleaned copy removes the duplicate row, keeps employee IDs as text, and leaves missing amounts empty.
- `lookup_benchmark.py`: compare the measured times; results vary by computer and should not be copied as fixed expected values.
- `logging_demo.py`: INFO and WARNING messages appear, and the ERROR example includes a traceback.

Record your own observed output and what you learned after running each exercise. Do not write that an exercise passed until you have run it yourself.
