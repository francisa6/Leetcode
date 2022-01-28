
class BinarySearchSolution:
    # O(log n) time complexity and O(1) space complexity
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid**2 == x or (mid**2 < x and (mid + 1)**2 > x):
                return mid
            elif mid**2 < x:
                l = mid + 1
            else:
                r = mid - 1


class NewtonRaphsonSolution:
    # O(log(n)F(n,m)), where F(n,m) is the cost of calculating f(x)/f'(x) with m-digit precision, time complexity 
    # and O(1) space complexity.
    # Find solution to f(r) = r**2 - x = 0. Can use Newton Raphson algo to find the closest approximation!
    # It won't run in an infinite loop because we are taking floor integer division
    def mySqrt(self, x: int) -> int:
        r = x
        while r**2 > x:
            r = (r + x // r) // 2
        return r

x = 64
print(BinarySearchSolution().mySqrt(x))

x = 64
print(NewtonRaphsonSolution().mySqrt(x))