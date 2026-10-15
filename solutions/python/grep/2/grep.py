
"""Implement a simplified grep command."""


def grep(pattern, flags, files):
    """Search files for lines matching a fixed string."""
    results = []
    multiple_files = len(files) > 1

    for filename in files:
        with open(filename, encoding="utf-8") as file:
            lines = file.readlines()

        file_has_match = False

        for line_number, line in enumerate(lines, start=1):
            text = line.rstrip("\n")

            if matches_pattern(text, pattern, flags):
                file_has_match = True

                if "-l" not in flags:
                    output = format_line(
                        filename,
                        text,
                        line_number,
                        multiple_files,
                        flags,
                    )
                    results.append(output)

        if "-l" in flags and file_has_match:
            results.append(filename)

    return "".join(result + "\n" for result in results)


def matches_pattern(text, pattern, flags):
    """Check whether a line matches the search criteria."""
    if "-i" in flags:
        text = text.lower()
        pattern = pattern.lower()

    if "-x" in flags:
        matched = text == pattern
    else:
        matched = pattern in text

    return not matched if "-v" in flags else matched


def format_line(filename, text, line_number, multiple_files, flags):
    """Add filename and line number prefixes when requested."""
    prefix = ""

    if multiple_files:
        prefix = f"{filename}:"

    if "-n" in flags:
        prefix += f"{line_number}:"

    return prefix + text
