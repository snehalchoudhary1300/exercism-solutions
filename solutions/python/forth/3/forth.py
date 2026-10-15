"""Evaluate a simple Forth program."""

import re


class StackUnderflowError(Exception):
    """Raised when the stack does not contain enough items."""


def evaluate(input_data):
    """Evaluate Forth instructions and return the final stack."""
    stack = []
    words = {}

    def require_items(count):
        if len(stack) < count:
            raise StackUnderflowError(
                "Insufficient number of items in stack"
            )

    def binary_operation(function):
        require_items(2)
        second = stack.pop()
        first = stack.pop()
        stack.append(function(first, second))

    def divide():
        require_items(2)
        second = stack[-1]

        if second == 0:
            raise ZeroDivisionError("divide by zero")

        stack.pop()
        first = stack.pop()
        quotient = abs(first) // abs(second)

        if (first < 0) != (second < 0):
            quotient = -quotient

        stack.append(quotient)

    def duplicate():
        require_items(1)
        stack.append(stack[-1])

    def drop():
        require_items(1)
        stack.pop()

    def swap():
        require_items(2)
        stack[-1], stack[-2] = stack[-2], stack[-1]

    def over():
        require_items(2)
        stack.append(stack[-2])

    operations = {
        "+": lambda: binary_operation(lambda first, second: first + second),
        "-": lambda: binary_operation(lambda first, second: first - second),
        "*": lambda: binary_operation(lambda first, second: first * second),
        "/": divide,
        "dup": duplicate,
        "drop": drop,
        "swap": swap,
        "over": over,
    }

    def define_word(tokens, index):
        if index + 2 >= len(tokens):
            raise ValueError("illegal operation")

        name = tokens[index + 1].lower()

        if re.fullmatch(r"[+-]?\d+", name) or name in {":", ";"}:
            raise ValueError("illegal operation")

        definition = []
        index += 2

        while index < len(tokens) and tokens[index] != ";":
            definition.append(tokens[index].lower())
            index += 1

        if index == len(tokens) or not definition:
            raise ValueError("illegal operation")

        expanded = []
        for word in definition:
            expanded.extend(words[word] if word in words else [word])

        words[name] = expanded
        return index + 1

    def execute(tokens):
        index = 0

        while index < len(tokens):
            token = tokens[index].lower()

            if token == ":":
                index = define_word(tokens, index)
                continue

            if re.fullmatch(r"[+-]?\d+", token):
                stack.append(int(token))
            elif token in words:
                execute(words[token])
            elif token in operations:
                operations[token]()
            else:
                raise ValueError("undefined operation")

            index += 1

    for line in input_data:
        execute(line.split())

    return stack