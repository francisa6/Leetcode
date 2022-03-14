

def fib(i: int):
    if i == 1:
        return 1

    return fib(i-1) * i  


def fib_tailrecursion(i: int):
    def fibsub(i: int, acc: int):
        if i == 1:
            return acc 
        return fibsub(i-1, acc * i)

    return fibsub(i, 1)

i = 3
print(fib(i))
print(fib_tailrecursion(i))