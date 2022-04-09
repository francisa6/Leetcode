from typing import List

class MyQueue:
    def __init__(self):
        self._queue = []

    def push(self, x: int) -> None:
        self._queue.append(x)

    def restack(self, _queue) -> List[int]:
        _queue_temp = [0]*len(_queue)
        for i in range(len(_queue)):
            _queue_temp[i] = _queue[len(_queue) - 1 - i]
        return _queue_temp
        
    def pop(self) -> int:
        # each element gets moved twice!
        _queue_temp = self.restack(self._queue)
        val = _queue_temp.pop()
        self._queue = self.restack(_queue_temp)
        return val

    def peek(self) -> int:
        return self.restack(self._queue)[-1]

    def empty(self) -> bool:
        return len(self._queue) == 0


class MyQueueMoreEfficient:
    def __init__(self):
        self._queue = []
        self._queue_temp = []

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        # each element gets moved once! So amortised cost == O(1)
        self.peek()
        return self._queue_temp.pop()

    def peek(self) -> int:
        if len(self._queue_temp) == 0: # still select top of self._queue_temp if it's not empty
            num_to_add = len(self._queue)
            for _ in range(num_to_add):
                self._queue_temp.append(self._queue.pop())
        return self._queue_temp[-1]

    def empty(self) -> bool:
        return len(self._queue) == 0 and len(self._queue_temp) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()