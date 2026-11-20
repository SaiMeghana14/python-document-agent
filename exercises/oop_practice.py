class Document:

    def __init__(self, name, file_type):
        self.name = name
        self.file_type = file_type

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.file_type == other.file_type
        )

doc1 = Document("meeting_notes.md", "Markdown")
doc2 = Document("meeting_notes.md", "Markdown")

print(doc1 == doc2)

name = "meeting_notes.md"
print(hash(name))