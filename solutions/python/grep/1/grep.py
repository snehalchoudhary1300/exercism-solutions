
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
            search_text = text
            search_pattern = pattern

            if "-i" in flags:
                search_text = search_text.lower()
                search_pattern = search_pattern.lower()

            if "-x" in flags:
                matches = search_text == search_pattern
            else:
                matches = search_pattern in search_text

            if "-v" in flags:
                matches = not matches

            if matches:
                file_has_match = True

                if "-l" in flags:
                    continue

                output = text

                if multiple_files:
                    output = f"{filename}:{output}"

                if "-n" in flags:
                    if multiple_files:
                        prefix, content = output.split(":", 1)
                        output = f"{prefix}:{line_number}:{content}"
                    else:
                        output = f"{line_number}:{output}"

                results.append(output)

        if "-l" in flags and file_has_match:
            results.append(filename)

    return "".join(result + "\n" for result in results)
