# O(exp(n))
def fib_a(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_a(n - 1) + fib_a(n - 2)

# O(n)


def fib_b(n):
    cache = {}

    def recursion(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in cache:
                return cache[n]
            result = recursion(n - 1) + recursion(n - 2)
            cache[n] = result
            return result
    return recursion(n)


def fib_i(n):
    x = 0
    y = 1
    for _ in range(n):
        x, y = y, x + y
    return x
