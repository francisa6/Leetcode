from typing import List

class MergeSort:
    def main(self, x):
        # base case
        if len(x) > 1:
            # split your array
            mid = len(x)//2
            l = self.main(x[:mid])
            r = self.main(x[mid:])

            # combine the reuslts together
            ptr_l, ptr_r = 0, 0
            for i in range(len(x)):
                if (ptr_l < len(l) and ptr_r < len(r)):
                    if (l[ptr_l] < r[ptr_r]):
                        x[i] = l[ptr_l]
                        ptr_l +=1
                    else:
                        x[i] = r[ptr_r]
                        ptr_r +=1
                
                elif ptr_r >= len(r):
                    x[i:] = l[ptr_l:]
                    break
                else:
                    x[i:] = r[ptr_r:]
                    break            
        return x

import random 
org_array = [random.randint(2,10) for _ in range(100)]
print('Original: ', org_array)
print('Sorted: ', MergeSort().main(org_array))

