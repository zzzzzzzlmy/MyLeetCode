'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

#Code is here

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if None == nums:
            return 0

        temp = res = nums[0]
        for num in nums[1:]:
            temp = max(num, temp + num)
            res = max(res, temp)

        return res
