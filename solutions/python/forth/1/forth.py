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

    def execute(tokens):
        index = 0

        while index < len(tokens):
            token = tokens[index].lower()

            if token == ":":
                if index + 2 >= len(tokens):
                    raise ValueError("illegal operation")

                name = tokens[index + 1].lower()

                if re.fullmatch(r"[+-]?\d+", name):
                    raise ValueError("illegal operation")

                if name in (":", ";"):
                    raise ValueError("illegal operation")

                definition = []
                index += 2

                while index < len(tokens) and tokens[index] != ";":
                    definition.append(tokens[index].lower())
                    index += 1

                if index == len(tokens) or not definition:
                    raise ValueError("illegal operation")

                # Store a copy so later redefinitions do not change old words.
                resolved_definition = []

                for word in definition:
                    if word in words:
                        resolved_definition.extend(words[word])
                    else:
                        resolved_definition.append(word)

                words[name] = resolved_definition
                index += 1
                continue

            if re.fullmatch(r"[+-]?\d+", token):
                stack.append(int(token))

            elif token in words:
                execute(words[token])

            elif token == "+":
                require_items(2)
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)

            elif token == "-":
                require_items(2)
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)

            elif token == "*":
                require_items(2)
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)

            elif token == "/":
                require_items(2)
                second = stack.pop()

                if second == 0:
                    raise ZeroDivisionError("divide by zero")

                first = stack.pop()
                quotient = abs(first) // abs(second)

                if (first < 0) != (second < 0):
                    quotient = -quotient

                stack.append(quotient)

            elif token == "dup":
                require_items(1)
                stack.append(stack[-1])

            elif token == "drop":
                require_items(1)
                stack.pop()

            elif token == "swap":
                require_items(2)
                stack[-1], stack[-2] = stack[-2], stack[-1]

            elif token == "over":
                require_items(2)
                stack.append(stack[-2])

            else:
                raise ValueError("undefined operation")

            index += 1

    for line in input_data:
        execute(line.split())

    return stack