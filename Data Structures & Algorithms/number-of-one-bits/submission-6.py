class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            # remove the rightmost 1 bit
            # eg 110110
            # the bit at position 2 from the end is removed
            # n becomes 1101 (I TIHNK)
            # BUT WHY IS ITHIS O(1) TIME
            # SEE AGAIN
            n &= n - 1
            res += 1
        return res