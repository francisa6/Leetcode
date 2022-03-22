class TreeNode:
    def __init__(self, val, count = 1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.size = len(nums)

        # Initialise the BST
        # Base case - when nums is len = 0
        self.root = None
        self.prevKLargestVal = None

        if self.size > 0 :
            for v in nums[:k]:
                self.insertion(self.root, v)

            self.prevKLargestVal = self.findKthLargest(self.root)
            
            # Update for the remaining values in nums list
            for v in nums[k:]:
                self.prevKLargestVal = self.add(v)
            
    def findKthLargest(self, currNode):
        while currNode.left:
            currNode = currNode.left
        return currNode.val

    def deleteLargest(self, currNode):
        # Base cases
        if not currNode:
            return

        if not currNode.left:
            self.root = currNode.right
            return 

        while currNode:
            
            if not currNode.left.left:
                currNode.left = currNode.left.right
                # currNode.left = None
                break
            currNode = currNode.left
        return

    def insertion(self, root, val: int):
        # Need to handle dups
        currNode = root
        if not currNode:
            self.root = TreeNode(val)
            return 

        while currNode:
            prevNode = currNode
            if currNode.val < val:
                currNode = currNode.right
                if not currNode:
                    prevNode.right = TreeNode(val)
            else:
                currNode = currNode.left
                if not currNode:
                    prevNode.left = TreeNode(val)
        return 

    def add(self, val: int) -> int:

        # Insertion
        # Find the kth largest val using the last value
        if  self.size < self.k or val > self.prevKLargestVal:
            
            if self.size >= self.k: self.deleteLargest(self.root)
            self.size +=1
            self.insertion(self.root, val)
            self.prevKLargestVal = self.findKthLargest(self.root)
        return self.prevKLargestVal


import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        
        # Add to heap
        heapq.heappush(self.heap, val)

        # Delete minimum from heap and rearrange into heap format
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Return the minimum
        return self.heap[0]
