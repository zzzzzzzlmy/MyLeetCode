#Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x  
        result = 0  
        while num > 0:  
            result = result * 10 + num % 10  
            num /= 10  
  
        return result == x 
