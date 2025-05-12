


def trim_md(content: str) -> str:
    if content.startswith("```markdown\n"):
        content = content[14:]
    elif content.startswith("```md\n"):
        content = content[13:]
    if content.endswith("```"):
        content = content[:-3]
    return content
