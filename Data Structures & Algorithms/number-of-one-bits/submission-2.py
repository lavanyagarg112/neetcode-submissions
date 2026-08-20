class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # bit masking

        # check each bit position one by one
        # check if it is set (1) or not (0)

        result = 0

        for i in range(32):
            if (1 << i) & n:
                result += 1

        return result