class Solution:
    def __init__(self):
        self.cost = []
        self.n = 0
        self.memo = {}

    def minCostClimb(self, index):
        if index >= self.n:
            return 0

        if index in self.memo:
            return self.memo[index]

        ans = self.cost[index] + min(self.minCostClimb(index + 1), self.minCostClimb(index + 2))
        self.memo[index] = ans
        return ans

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.n = len(cost)
        return min(self.minCostClimb(0), self.minCostClimb(1))
        
        