class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # dp
        # numbers repeat their bit patterns every time we reach
        # power of 2
        # when power of 2: exactly one bit
        # thus bits in ith num = 1 (for highest power of 2) + number of bits in remainder -- dp

        dp = [0] * (n+1)
        offset = 1 # curr power of two

        for i in range(1, n+1):
            if 2 ** (offset+1) == i:
                offset += 1
                dp[i] = 1
            else:
                dp[i] = 1 + dp[i - 2**offset]

        return dp
            