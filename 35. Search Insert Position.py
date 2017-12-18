'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if None == nums:  
            return 0  
        len_nums = len(nums)  
        if target > nums[len_nums - 1]:  
            return len_nums  
        if target < nums[0]:  
            return 0  
  
        left = 0  
        right = len_nums - 1  
        while left <= right:    
            mid = (left + right) / 2  
            if nums[mid] < target:  
                left = mid + 1  
            elif nums[mid] > target:  
                right = mid - 1  
            else:  
                return mid  
        return left  
    
