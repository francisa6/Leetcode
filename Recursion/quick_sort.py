import random

class Solution:
    def quickSort(self, x):

        if len(x) > 1:
            # Just take the last value as the pivot 
            pivot = x[-1]
            less_pivot, greater_pivot= [], []
            for i in x[:-1]:
                if i < pivot:
                    less_pivot.append(i)
                else:
                    greater_pivot.append(i)

            x = self.quickSort(less_pivot) + [pivot] + self.quickSort(greater_pivot)

        return x

import random 
x  = [random.randint(1,1000) for _ in range(100)]
print('Org: ', x)
print('Sorted: ', Solution().quickSort(x))
