'''
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.
'''

#Example
#Input: 4        Input: 8
#Output: 2       Output: 2

#Code is here
#1
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        i = 0
        j = x
        mid = 0
        while True:
            mid=(i + j) / 2
            if mid > x / mid:
                j = mid
            else:
                if(mid + 1) > x / (mid + 1):
                    return mid
                i = mid
                
                
#2
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = x
        while i * i > x:
            i = (i + x / i) / 2
        return i
    
    
    


