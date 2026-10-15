import itertools
import re


def solve(puzzle):
    """Solve an alphametics puzzle."""
    words = re.findall(r"[A-Z]+", puzzle)
    unique_letters = list(set("".join(words)))
    
    if len(unique_letters) > 10:
        return None

    leading_letters = {word[0] for word in words}
    *addends, result = words

    for perm in itertools.permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))

        if any(mapping[letter] == 0 for letter in leading_letters):
            continue

        total_addends = 0
        for word in addends:
            num = 0
            for char in word:
                num = num * 10 + mapping[char]
            total_addends += num

        res_num = 0
        for char in result:
            res_num = res_num * 10 + mapping[char]

        if total_addends == res_num:
            return mapping

    return None