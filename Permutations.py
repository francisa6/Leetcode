
# char_list = ['a', 'b', 'c']

def get_strings(C):
    if len(C) == 0:
        return [""]
    else:
        return [c + s for c in C for s in get_strings([a for a in C if a != c])]


def get_strings(C):
    if len(C) == 0:
        return [""]
    else:
        return [c + s for c in C for s in get_strings([a for a in C if a != c])]


def perm(i):
    if i == 0:
        return [""]
    else:
        results = []
        for c in char_list:
            for t in perm(i - 1):
                results.append(c + t)
        return results


if False:
    char_list = ['a', 'b', 'c']

    def get_strings(s, n, char_list_temp):
        if n == 0:
            print(s)
        else:
            for c in char_list_temp:
                get_strings(s + c, n-1, [d for d in char_list_temp if d != c])

    get_strings("", 3, char_list)


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

# set_n_given_nm1(C, S, 3)


def perm_Set(C):

    if len(C) == 0:
        return [""]
    else:
        return [c + s for c in C for s in perm_Set([s for s in C if s != c])]

# perm_Set(char_list)


def perm_Set(S: list, char_list: list) -> list:

    S_new = [s + c for s in S for c in char_list if c not in list(s)]
    if len(S_new[0]) == len(char_list):
        return S_new
    else:
        return perm_Set(S_new, char_list)


def perm_Set_2(char_list: list) -> list:
    S = [""]
    for _ in range(len(char_list)):
        S = [s + c for s in S for c in char_list if c not in list(s)]
    return S


char_list = ['a', 'b', 'c', 'd']
hi = perm_Set(char_list, char_list)
print(hi)
print(len(hi))
