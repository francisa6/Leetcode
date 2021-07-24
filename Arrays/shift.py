from typing import List


# Rotate right by one position in-place
#
# xs = [1, 2, 3, 4]
# rotateRight(xs)
# print(xs) -> [4, 1, 2, 3]
def rotateRight(xs: List[int]):
    print("rotateRight sees", id(xs))
    if True:
        last = xs[-1]
        for i in range(len(xs) - 1, 0, -1):
            xs[i] = xs[i - 1]
        xs[0] = last
    else:
        next_val = xs[-1]
        for i in range(len(xs)):
            xs[i], next_val = next_val, xs[i]


# Rotate left by one position in-place
#
# xs = [1, 2, 3, 4]
# rotateLeft(xs)
# print(xs) -> [2, 3, 4, 1]
def rotateLeft(xs: List[int]):
    if True:
        first = xs[0]
        for i in range(len(xs) - 1):
            xs[i] = xs[i + 1]
        xs[-1] = first
    else:
        next_val = xs[0]
        for i in range(len(xs) - 1, -1, -1):
            xs[i], next_val = next_val, xs[i]


xs = [1, 2, 3, 4]
ys = xs.copy()
print("address of xs is", id(xs))
print("i copied and got", id(xs.copy()))

blah = xs.copy()
rotateRight(blah)
foo = xs.copy()
rotateLeft(foo)

print(blah)
print(foo)
# print("rotateRight([1, 2, 3, 4]) =", xs)
# xs = [1, 2, 3, 4]
# rotateLeft(xs)
# print("rotateLeft([1, 2, 3, 4]) =", xs)
