class NaiveMyHashMap:
    def __init__(self):
        self.hashMap = [[] for _ in range(10**6 + 1)]
        self.hash = lambda key: key % (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hashMap[self.hash(key)] = [value] 

    def get(self, key: int) -> int:
        if len(self.hashMap[self.hash(key)]) > 0:
            return self.hashMap[self.hash(key)][0]
        return -1
    def remove(self, key: int) -> None:
        self.hashMap[self.hash(key)] = []
        
class MyHashMap:
    def hash(self, key):
        # multiplicative hash
        # floor[(aK mod 2**w)/2^(w-m)], where a = 1031237, w = 20, m = 15
        # Note that the mod can be evaluated as: s % (2^t) = s & (1<<t) - 1
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        # self.m = 60 # size of hashMap
        self.hashMap = [[] for _ in range(1<<15)]
     
    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.hashMap[self.hash(key)].append((key, value))

    def get(self, key: int) -> int:
        for t in self.hashMap[self.hash(key)]:
            if key == t[0]:     
                return t[1]
        return -1

    def remove(self, key: int) -> None:
        for e, t in enumerate(self.hashMap[self.hash(key)]):
            if key == t[0]:
                del self.hashMap[self.hash(key)][e]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)