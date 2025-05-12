import os
from src.shared.cfg import OBSIDIAN_STD_DB_LOC


def read_filenames_from_database(loc: str = OBSIDIAN_STD_DB_LOC) -> list[str]:
    """
    Recursively returns a list of filenames in the database folder,
    joining files with their relative folder path.

    Example:
    folder structure:
    core/
      file1.md
      file2.md
      proves/
        file3.md
    main.md

    Returns: ["core/file1.md", "core/file2.md", "core/proves/file3.md", "main.md"]
    """
    def recursive_read(current_path: str, base_path: str) -> list[str]:
        result = []
        for item in os.listdir(current_path):
            if item == ".DS_Store":
                continue

            full_path = os.path.join(current_path, item)
            relative_path = os.path.relpath(full_path, base_path)

            if os.path.isdir(full_path):
                result.extend(recursive_read(full_path, base_path))
            elif item.endswith(".md"):
                result.append(relative_path)

        return result

    return sorted(recursive_read(loc, loc))


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
