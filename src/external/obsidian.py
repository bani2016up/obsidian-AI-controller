import os
from src.shared.cfg import OBSIDIAN_STD_DB_LOC


def read_filenames_from_database(loc: str = OBSIDIAN_STD_DB_LOC) -> list[str]:
    """
    returns a list of filenames in std database folder,
    joins files with folder path
    example:
    core:
      - file1.md
      - file2.md
    main.md
    -> ["core/file1.md", "core/file2.md", "main.md"]
    """
    dirs: list[str] = os.listdir(loc)
    if ".DS_Store" in dirs:
        dirs.remove(".DS_Store")
    return [
        os.path.join(dir, file)
        for dir in dirs
        for file in os.listdir(os.path.join(loc, dir))
        if file.endswith(".md")
    ]


def create_document(content: str, location: str = OBSIDIAN_STD_DB_LOC) -> None:
    """
    Creates a new document in the specified location.
    """
    # ? note that document title does not impact the filename,
    # ? as obsidian will rename it according to first row in the document
    with open(os.path.join(location, "new.md"), "w") as f:
        f.write(content)


def read_document(filename: str, location: str = OBSIDIAN_STD_DB_LOC) -> str:
    """
    Reads the content of a document from the specified location.
    """
    with open(os.path.join(location, filename), "r") as f:
        return f.read()

def write_document(filename: str, content: str, location: str = OBSIDIAN_STD_DB_LOC) -> None:
    """
    Writes the content to a document in the specified location.
    """
    with open(os.path.join(location, filename), "w") as f:
        f.write(content)
