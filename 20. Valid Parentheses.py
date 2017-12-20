'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp = {')': '(', ']': '[', '}': '{'}  
        stack = []  
        for ch in s:  
            if ch in '([{':  
                stack.append(ch)  
            else:  
                if not stack or mp[ch] != stack.pop():  
                    return False  
        return not stack 
