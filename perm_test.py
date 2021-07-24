
def get_next_perm(s: str):

    # find the index (i) where it is larger than the last couple of values

    list_s = list(s)
    for i in range(len(list_s) - 1, -1, -1):
        if list_s[i] > list_s[i-1]:
            break
        else:
            i -= 1

    if i == 0:
        return s[::-1]

 # swap the i-1 value with the list of values from [i:] that is just slightly larger than it
 # first find the index that is true
 # then swap
    post_list_greater_previ = [
        (c, i + k) for k, c in enumerate(list_s[i:]) if list_s[i-1] < c]
    min_index = min(post_list_greater_previ)[1]
    list_s[i - 1], list_s[min_index] = list_s[min_index], list_s[i - 1]
    list_s[i:] = reversed(list_s[i:])
    return "".join(list_s)


def get_all_perms(s):
    results = []
    start = s
    while True:
        results.append(s)
        s = get_next_perm(s)
        if s == start:
            break
    return results
