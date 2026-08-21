class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = stones[0]
        for i in range(1, len(stones)):
            curr = abs(res - stones[i])
            res = curr

        return res
        