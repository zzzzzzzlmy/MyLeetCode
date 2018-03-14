'''
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=[]
        for i in set(s):
            if s.count(i) == 1:
                lst.append(s.index(i))
        if len(lst) > 0:
            return min(lst)
        else:
            return -1
            
            
