class Node:
    def __init__(self, key, val, next = None):
        self.key = key 
        self.value = val
        self.next = next


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.hashmap = [Node(-1, -1, None) for _ in range(self.buckets)]
        
    def hashfunc(self, key) -> int:
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # Instead can also use self.remove(key) and then add a new key in, in the front
        hashval = self.hashfunc(key)

        currNode = self.hashmap[hashval]
        preNode = currNode
        while currNode:
            if key == currNode.key:
                currNode.value = value
                return
            preNode = currNode
            currNode = currNode.next
        preNode.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashval = self.hashfunc(key)

        currNode = self.hashmap[hashval]
        while currNode:
            if key == currNode.key:
                return currNode.value
            currNode = currNode.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashval = self.hashfunc(key)

        currNode = self.hashmap[hashval]
        while currNode:

            if key == currNode.key:
                prevNode.next = currNode.next
                return 
            
            prevNode = currNode
            currNode = currNode.next
        
        

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)