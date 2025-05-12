import os
import traceback
from src.shared.cfg import OBSIDIAN_STD_DB_LOC
from src.external.obsidian import read_filenames_from_database, create_document, read_document, write_document
from src.domain.chat_model import make_single_request
from src.domain.prompts import create_db_doc, refactor_document
from src.shared.utils import trim_md

def create_database_record(folder: str, topic: str, loc: str = OBSIDIAN_STD_DB_LOC) -> None:
    existing_files: list[str] = read_filenames_from_database(loc)
    try:
        document_content: str = trim_md(make_single_request(
            create_db_doc(formatters=[topic, existing_files])
        ))
    except Exception as e:
        traceback.print_exc()
        return
    create_document(document_content, loc+folder)


def read_document_and_format_to_md(filename: str, loc: str = OBSIDIAN_STD_DB_LOC) -> None:
    content = read_document(filename, loc)
    try:
        formatted_content: str = trim_md(make_single_request(
            refactor_document(formatters=[content])
        ))
        write_document(filename, formatted_content, loc)
    except Exception as e:
        traceback.print_exc()
        return
