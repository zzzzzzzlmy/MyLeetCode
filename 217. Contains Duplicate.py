'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value 
appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in xrange(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
        
