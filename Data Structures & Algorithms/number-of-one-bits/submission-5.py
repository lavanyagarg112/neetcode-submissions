class Solution:
    def hammingWeight(self, n: int) -> int:
        
        result = 0

        while n != 0:
            # check the last bit
            if n & 1:
                result += 1
            # shift n to the right
            # eg 0101 -> 010 (the 1 at right most is removed)
            n = n >> 1

        return result
