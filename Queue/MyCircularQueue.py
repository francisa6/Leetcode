# Remember to add the paratheses in self.isFull() and remember to adjust the head and tail elements
# after removing from an array of size = 1. Also remember to add conditions if dividing/taking modulus by zero.


class MyCircularQueue:
    def __init__(self, k: int):
        # k is the size of the queue
        self.maxsize = k
        self.size = 0
        self.queue = [None] * k

        # pointer to the start of the queue -- when we add an elt self.head should be 0
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        if self.size == 0:
            self.head += 1

        self.tail = (self.tail + 1) % self.maxsize
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.head] = None
        if self.tail == self.head:
            self.head, self.tail = -1, -1
        else:
            self.head = (self.head + 1) % self.maxsize
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size != 0:
            return self.queue[self.head]
        return -1

    def Rear(self) -> int:
        if self.size != 0:
            return self.queue[self.tail]
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if ((self.tail + 1) % self.maxsize) == self.head:

            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
k = 6
value = 4

obj = MyCircularQueue(k)
param_1 = obj.enQueue(value)
param_7 = obj.enQueue(3)
param_8 = obj.enQueue(5)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

print(
    "The Queue elements are: ",
    list(obj.queue),
    "size",
    obj.size,
    "head",
    obj.head,
    "tail",
    obj.tail,
    "front",
    param_3,
    "rear",
    param_4,
)
