class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = [0] * (n+1)

        for num in range(1, n+1):
            curr = 0
            for i in range(32):
                if (1 << i) & num:
                    curr += 1
            output[num] = curr

        return output
