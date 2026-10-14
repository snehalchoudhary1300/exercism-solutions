
"""Evaluate simple math word problems."""


def answer(question):
    """Return the result of a math word problem."""
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    words = question[8:-1].split()

    if not words:
        raise ValueError("syntax error")

    try:
        result = int(words[0])
    except ValueError:
        raise ValueError("syntax error") from None

    index = 1

    while index < len(words):
        operation = words[index]

        if operation not in ("plus", "minus", "multiplied", "divided"):
            if operation in ("by",):
                raise ValueError("syntax error")
            if operation.lstrip("-").isdigit():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        index += 1

        if operation in ("multiplied", "divided"):
            if index >= len(words) or words[index] != "by":
                raise ValueError("syntax error")
            index += 1

        if index >= len(words):
            raise ValueError("syntax error")

        try:
            number = int(words[index])
        except ValueError:
            raise ValueError("syntax error") from None

        if operation == "plus":
            result += number
        elif operation == "minus":
            result -= number
        elif operation == "multiplied":
            result *= number
        else:
            if number == 0:
                raise ValueError("division by zero")
            result = int(result / number)

        index += 1

    return result
