from dataclasses import dataclass


@dataclass
class Note:
    title: str
    body: str

if __name__ == "__main__":
    note = Note("First note", "This is a small dataclass example.")
    print(note.title)
    print(note.body)
