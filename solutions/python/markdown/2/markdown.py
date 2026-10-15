
"""Parse Markdown text and convert it to HTML."""


def parse(markdown):
    """Convert Markdown headings, lists, and paragraphs to HTML."""
    lines = markdown.split("\n")
    result = []
    in_list = False
    in_paragraph = False

    for line in lines:
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))

            if 1 <= level <= 6 and line[level:level + 1] == " ":
                close_blocks(result, in_list, in_paragraph)
                in_list = False
                in_paragraph = False

                content = line[level + 1:]
                result.append(
                    f"<h{level}>{format_text(content)}</h{level}>"
                )
                continue

        if line.startswith("* "):
            if in_paragraph:
                result.append("</p>")
                in_paragraph = False

            if not in_list:
                result.append("<ul>")
                in_list = True

            result.append(f"<li>{format_text(line[2:])}</li>")
            continue

        if line.strip():
            if in_list:
                result.append("</ul>")
                in_list = False

            if not in_paragraph:
                result.append("<p>")
                in_paragraph = True
            else:
                result.append(" ")

            result.append(format_text(line))
        else:
            close_blocks(result, in_list, in_paragraph)
            in_list = False
            in_paragraph = False

    close_blocks(result, in_list, in_paragraph)
    return "".join(result)


def close_blocks(result, in_list, in_paragraph):
    """Close open lists and paragraphs."""
    if in_list:
        result.append("</ul>")
    if in_paragraph:
        result.append("</p>")


def format_text(text):
    """Convert only valid Markdown emphasis markers to HTML."""
    result = []
    index = 0

    while index < len(text):
        if text.startswith(("__", "**"), index):
            marker = text[index:index + 2]
            closing = text.find(marker, index + 2)

            if closing != -1:
                result.append("<strong>")
                result.append(text[index + 2:closing])
                result.append("</strong>")
                index = closing + 2
                continue

        if text[index] in {"_", "*"}:
            marker = text[index]
            closing = text.find(marker, index + 1)

            if closing != -1:
                result.append("<em>")
                result.append(text[index + 1:closing])
                result.append("</em>")
                index = closing + 1
                continue

        result.append(text[index])
        index += 1

    return "".join(result)
