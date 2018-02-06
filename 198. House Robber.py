'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums[0], nums[-1])
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            res[i] = max(nums[i] + res[i-2], res[i-1])
        return res[len(nums)-1]
        
        
