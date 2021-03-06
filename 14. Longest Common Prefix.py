#Write a function to find the longest common prefix string amongst an array of strings.

'''Example:
Given strs = ['ab','abc','abuh','abcd','abcss','abg']
return 'ab'
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        res = ''
        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
