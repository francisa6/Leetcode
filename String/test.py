
def f(x, i):
    print(x)
    if i ==0:
        return x
    return f(x+1, i-1)



print(f(2, 3))


def g(x):
    print('x', x)
    if x == 2:
        return x**2
    return g(x+1)

return_val = g(0)

print(return_val)