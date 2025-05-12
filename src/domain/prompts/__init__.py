from typing import Callable
from . import features
from functools import partial

__all__ = ("create_db_doc", "give_title")


def feature_prompt(
    features: list[str] | None = None, formatters: list[str] | None = None
) -> str:

    if features is None:
        features = []
    if formatters is None:
        formatters = []

    prompt = " ".join(features)
    return prompt.format(*formatters)


create_db_doc: Callable = partial(
    feature_prompt,
    features=[
        features.standard_obsidian_db_doc,
        features.standard_obsidian_db_structure,
        features.obsidian_formatted,
        features.include_relation_to_other_docs,
    ],
)

give_title: Callable = partial(
    feature_prompt,
    features=[features.respond_with_title_for_content, features.limit_with_words_count],
)

refactor_document: Callable = partial(
    feature_prompt,
    features=[
        features.standard_obsidian_db_structure,
        features.refactor_document,
    ],
)
