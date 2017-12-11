'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        
        len1 = len(haystack)
        len2 = len(needle)
        if len1 < len2:
            return -1
        
        for i in range(len1 - len2 + 1):
            j = 0
            k = i
            while j < len2 and needle[j] == haystack[k]:
                j += 1
                k += 1
            
            if j == len2:
                return i
        
        return -1
