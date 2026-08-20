class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # bit masking

        # check each bit position one by one
        # check if it is set (1) or not (0)

        result = 0

        for i in range(32):

            # i << i sets the ith bit to 1 by shfiting 1 by i positions 
            # to the left
            # eg i = 0 -> 0001
            # i = 1 -> 0010
            # & n checks if that bit is also 1
            # because lhs all are 0 except ith position
            # the lhs and rhs are compared bit by bit
            # all non-i positions will be 0 since and with 0
            # only the ith position in lhs is 1
            # so in rhs also if its 1 then & is true
            # else & is false
            if (1 << i) & n:
                result += 1

        return result