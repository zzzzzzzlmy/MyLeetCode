'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''

#Example 1:
#Input: 1
#Output: "1"

#Example 2:
#Input: 4
#Output: "1211"

#Code is here
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s = '1'
        for i in range(1, n):
            s = self.next(s)
        return s
        
    def next(self,s):          
        count = 1
        res = ''
        for i, ch in enumerate(s):
            if i + 1 < len(s) and s[i] != s[i+1]:
                res = res + str(count) + ch
                count = 1
            elif i + 1 < len(s):
                count = count + 1
                
        res = res + str(count) + ch    
        return res
