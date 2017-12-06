'''
Given an array of integers, every element appears twice except for one. Find that single one.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res
        
        
