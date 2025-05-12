from src.domain.services.obsidian import create_database_record, read_document_and_format_to_md
from src.external.obsidian import read_filenames_from_database

def main():
    while True:
        mode = int(input("Choose mode (1 - new doc/2 - refactor old): "))
        if mode == 1:
            topic = input("Enter a topic or 'exit' to quit: ")
            if topic.lower() == 'exit':
                break
            folder = input("Enter the folder name: ")
            create_database_record(folder, topic)
            print("Database record created successfully.")
        elif mode == 2:
            files_map = dict(enumerate(read_filenames_from_database()))
            print(files_map)
            select_file = input("Enter the file ID to refactor (or 'exit' to quit): ")
            if select_file.lower() == 'exit':
                break
            if filename := files_map.get(int(select_file)):
                read_document_and_format_to_md(filename)
                print("Document refactored successfully.")
