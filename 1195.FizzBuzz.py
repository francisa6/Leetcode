"""
Acquire a lock to access data that is guarded by that lock. 
Release the lock once the thread completes changing the shared variable
"""
import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        # instantiate the lock class objects - has unlocked (also known as released) 
        # status unless acquired. Want to acquire all 3 locks except main because
        # we want main to be locked.
        self.f = threading.Lock()
        self.b = threading.Lock()
        self.fb = threading.Lock()
        self.main = threading.Lock()
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()

        print(self.main)


    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                return
            printFizz()
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                return
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                return
            printFizzBuzz()
            self.main.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]', i: int) -> None:
            
        for i in range(1, 1 + self.n):
            self.main.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.f.release()
            elif i % 3 == 0:
                self.b.release()
            elif i % 5 == 0:
                self.fb.release()
            else:
                printNumber(i)
                self.main.release()

        self.main.acquire() 
        self.n = 0
        self.f.release()
        self.b.release()
        self.fb.release()
        return