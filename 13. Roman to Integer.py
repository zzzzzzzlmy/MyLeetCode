#Given a roman numeral, convert it to an integer.

#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  
        result = 0  
        i = 0
        while i < len(s):  
            if i > 0 and Roman[s[i]] > Roman[s[i - 1]]:  
                result += Roman[s[i]] - 2 * Roman[s[i - 1]]  
            else:  
                result += Roman[s[i]]  
            i += 1
        return result  
