'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[:1:-1]
        return int(b + '0'*(32-len(b)), 2)
        
        
