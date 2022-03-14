class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 15
        self.hash_set = [[] for _ in range(1<<self.numBuckets)]
    
    def hashfunc(self, key):
        return ((1031237 * key) & ((1 << 20) - 1)) >> 5

    def add(self, key: int) -> None:
        hashValue = self.hashfunc(key)
        if key not in self.hash_set[hashValue]:
            self.hash_set[hashValue].append(key)

    def remove(self, key: int) -> None:
        hashValue = self.hashfunc(key)
        if key in self.hash_set[hashValue]:
            self.hash_set[hashValue].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashValue = self.hashfunc(key)
        return key in self.hash_set[hashValue]
        

class MyHashSetPythonBase:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = set()

    def add(self, key: int) -> None:
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        self.hash_set.discard(key)        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hash_set
        
ownSet = MyHashSet()
print(
ownSet.add(1),
ownSet.add(2),
print(ownSet),
ownSet.remove(1),
ownSet,
ownSet.contains(1),
ownSet.contains(2),
ownSet,
)