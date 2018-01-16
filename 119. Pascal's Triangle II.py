'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst=[]
        for i in range(rowIndex + 1):
            lst.append([1] * (i+1))
            if i > 1:
                for j in range(1,i):
                    lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

        return lst[rowIndex][:]
        
        
