'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2]

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

#Code is here

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        nums_len = len(nums)
        while i < nums_len - 1:
            if nums[i] == nums[i+1]:
                del nums[i]
                nums_len -= 1
            else:
                i += 1
        return len(nums)
