"""
Sequence functions implementations
"""

from typing import Union


def is_palindrome(origin: Union[str, int], /) -> bool:
    def flipped(value):
        return value[::-1]

    if flipped(str(origin)) == str(origin):
        result = True
    else:
        result = False

    return result


assert is_palindrome("aba") is True
assert is_palindrome("abc") is False
assert is_palindrome(12345) is False
assert is_palindrome(12321) is True


def get_longest_palindrome(origin: str, /) -> str:
    res = []

    def flipped(value):
        return value[::-1]

    for i in range(len(origin)):
        for j in range(i + 1, len(origin) + 1):
            part = origin[i: j]
            if flipped(part) == part:
                res.append(part)

    return max(res, key=len)


assert get_longest_palindrome("0123219") == "12321"
assert get_longest_palindrome("1012210") == "012210"


def are_parentheses_balanced(origin: str, /) -> bool:
    opened_pattern = ['(', '{', '[']
    closed_pattern = [')', '}', ']']
    result = 0
    for i in origin:
        if i in opened_pattern:
            result += 1
        elif i in closed_pattern:
            result -= 1
        else:
            return False

    if result < 0:
        return False
    if result > 0:
        return False
    return True


assert are_parentheses_balanced("({[]})") is True
assert are_parentheses_balanced(")]}{[(") is False


def get_longest_uniq_length(origin: str, /) -> int:
    count = 0
    test = ''
    l = []

    for i in origin:
        if i not in test:
            test += i
            count += 1
            l.append(count)
        else:
            count = 0
            continue

    return max(l)


assert get_longest_uniq_length("abcalkfgh") == 5
assert get_longest_uniq_length("abcdefg") == 7
assert get_longest_uniq_length("racecar") == 4
