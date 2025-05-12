

standard_obsidian_db_doc: str = "User requested a record into hit personal database on the topic: {}"
standard_obsidian_db_structure: str = "This document must be of the following structure: Title, Definition, Explicit Construction [optional], Key Properties, Examples, Applications, other field depending on the topic."
obsidian_formatted: str = "Respond only with the document text optimized for Obsidian .md format, if document contains any math equations, use Latex and $$ symbols to declare it."
include_relation_to_other_docs: str = "The user has already created some documents in Obsidian. When replying, include links to these documents for better context. Use standard obsidian relation notation like [[#file-id|link-name]] for links. Here are all user files-ids: {}"""


limit_with_words_count: str = "Ensure the response does not exceed {} words."
respond_with_title_for_content: str =  "Read the following content and give a good title for it: {}. "


refactor_document: str = "Refactor the following document to improve its readability and content: {}"
