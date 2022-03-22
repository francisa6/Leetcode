"""
O(m) time complexity. At first glance looks like O(n) 
because we have a break and that we make i jump to the stop_index 
but we need to remember that result += inner_result * repeat_count 
would loop through the expanded results too.
"""

from typing import List, Tuple


def decode(s: str, i: int) -> (str, int):
    result = ""
    while i < len(s):
        c = s[i]
        if c == "]":
            i += 1
            break
        elif c >= "a" and c <= "z":
            i += 1
            result += c
        else:
            assert c >= "0" and c <= "9"
            bracket_index = s.find("[", i + 1)
            repeat_count = int(s[i:bracket_index])
            inner_result, stop_index = decode(s, bracket_index + 1)
            result += inner_result * repeat_count
            i = stop_index
    return result, i


class Solution:
    def decodeString(self, s: str) -> str:
        return decode(s, 0)[0]


class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decode() -> str:
            nonlocal i
            result = ""
            while i < len(s):
                c = s[i]
                if c == "]":
                    i += 1
                    break
                elif c >= "a" and c <= "z":
                    i += 1
                    result += c
                else:
                    assert c >= "0" and c <= "9"
                    bracket_index = s.find("[", i + 1)
                    repeat_count = int(s[i:bracket_index])
                    i = bracket_index + 1
                    inner_result = decode()
                    result += inner_result * repeat_count
            return result

        return decode()


class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        stack: List[Tuple[str, int]] = []
        result = ""
        while i < len(s):
            c = s[i]
            if c == "]":
                i += 1
                old_result, repeat_count = stack.pop()
                result = old_result + result * repeat_count
            elif c >= "a" and c <= "z":
                i += 1
                result += c
            else:
                assert c >= "0" and c <= "9"
                bracket_index = s.find("[", i + 1)
                repeat_count = int(s[i:bracket_index])
                i = bracket_index + 1
                stack.append((result, repeat_count))
                result = ""
        return result
