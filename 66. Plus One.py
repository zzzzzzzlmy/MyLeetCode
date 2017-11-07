'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
#eg. [1,2,3] -> [1,2,4] / [1,9,9] -> [2,0,0]

#Code is here

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
 
        tep = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + tep > 9:
                digits[i] = 0
                tep = 1
            else:
                digits[i] += tep
                tep = 0
        if tep == 1:
            digits.insert(0, 1)
        return digits
        
        
        
