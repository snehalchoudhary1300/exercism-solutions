
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

    operations = {
        "plus": lambda first, second: first + second,
        "minus": lambda first, second: first - second,
        "multiplied": lambda first, second: first * second,
        "divided": lambda first, second: int(first / second),
    }
    valid_operations = set(operations)

    index = 1

    while index < len(words):
        operation = words[index]

        if operation not in valid_operations:
            if operation.lstrip("-").isdigit() or operation == "by":
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        index += 1

        if operation in {"multiplied", "divided"}:
            if index >= len(words) or words[index] != "by":
                raise ValueError("syntax error")
            index += 1

        if index >= len(words):
            raise ValueError("syntax error")

        try:
            number = int(words[index])
        except ValueError:
            raise ValueError("syntax error") from None

        if operation == "divided" and number == 0:
            raise ValueError("division by zero")

        result = operations[operation](result, number)
        index += 1

    return result
