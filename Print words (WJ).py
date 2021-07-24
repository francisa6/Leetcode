char_list = ["a", "b", "c"]

# Prints all strings that start with s and also add on all possible
# n length strings containing char_list


def print_strings(n, s):
    if n == 0:
        print(s)
    else:
        for c in char_list:
            print_strings(n - 1, s + c)

# Returns a list of all strings s such that len(s) == n and for every character c
# in s, c is in char_list


def get_strings(n):
    if n == 0:
        return [""]
    else:
        return [c + s for c in char_list for s in get_strings(n - 1)]


def get_strings_accumulate(n):
    # n is number of characters left to "fill in"
    # s is the built up string so far
    def recursion(n, s, results):
        pad = "    " * len(s)
        print(f"{pad}recursion({n}, \"{s}\")")
        if n == 0:
            results.append(s)
        else:
            for c in char_list:
                recursion(n - 1, s + c, results)
    results = []
    recursion(n, "", results)
    return results


def annys_version(n):
    strs = [""]
    for _ in range(n):
        strs = [c + s for c in char_list for s in strs]
    return strs


def get_next_str(s):
    cs = list(s)
    for i in range(len(cs) - 1, -1, -1):
        if cs[i] != char_list[-1]:
            cs[i] = chr(ord(cs[i]) + 1)
            break
        else:
            cs[i] = char_list[0]
    return "".join(cs)


def get_strings_using_get_next_str(n):
    results = []
    start = "a" * n
    s = start
    while True:
        results.append(s)
        s = get_next_str(s)
        if s == start:
            break
    return results


def set_n_given_nm1(C, S, N):
    n = 0
    while True:
        S = [c + s for c in C for s in S]
        n += 1
        if n == N:
            print(S)
            break


S = [""]
C = char_list

set_n_given_nm1(C, S, 3)


# Permutation
def get_strings(C):
    if len(C) == 0:
        return [""]
    else:
        return [c + s for c in C for s in get_strings([a for a in C if a != c])]

C = char_list
C = ["a", "b", "c", "d", "e"]
get_strings(C)