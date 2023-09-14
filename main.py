"""
Sequence functions implementations
"""
import string
from typing import Union


def is_palindrome(origin: Union[str, int], /) -> bool:
    test = str(origin).lower()
    test = test.replace(' ', '')
    for i in test:
        if i in string.punctuation:
            test = test.replace(i, '')
    if str(test)[::-1] == str(test):
        result = True
    else:
        result = False
    return result


assert is_palindrome("palindrome") is False
assert is_palindrome("tattarrattat") is True
assert is_palindrome("malayalam") is True
assert is_palindrome(12345) is False
assert is_palindrome(12321) is True
assert is_palindrome("Serhii") is False
assert is_palindrome("Hannah") is True
assert is_palindrome("This is some sentence") is False
assert is_palindrome("Mr. Owl ate my metal worm") is True
assert is_palindrome("Satire: Veritas") is True
assert is_palindrome("Dammit I'm Mad") is True


def get_longest_palindrome(origin: str, /) -> str:
    res = []

    for i in range(len(origin)):
        for j in range(i + 1, len(origin) + 1):
            part = origin[i: j]
            if part[::-1] == part:
                res.append(part)

    return max(res, key=len)


assert get_longest_palindrome("0123219") == "12321"
assert get_longest_palindrome("1012210") == "012210"


def are_parentheses_balanced(origin: str, /) -> bool:
    opened_pattern = ['(', '{', '[', '<']
    closed_pattern = [')', '}', ']', '>']
    result = 0
    op_index = 0
    cp_index = 0
    for i in origin:
        if 0 != cp_index < op_index != 0:
            return False
        if i in opened_pattern:
            result += 1
            op_index = origin.index(i)
        elif i in closed_pattern:
            result -= 1
            cp_index = origin.index(i)
        elif i not in opened_pattern or closed_pattern:
            continue
        else:
            return False

    if result < 0:
        return False
    if result > 0:
        return False

    return True


assert are_parentheses_balanced("(some <text>)") is True
assert are_parentheses_balanced("") is True
assert are_parentheses_balanced("[(<)}{(>)]") is False
assert are_parentheses_balanced("[]]") is False
assert are_parentheses_balanced("(()") is False
assert are_parentheses_balanced("({[]})") is True


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
assert get_longest_uniq_length("hwccjayhiszbmomlqkem") == 11
