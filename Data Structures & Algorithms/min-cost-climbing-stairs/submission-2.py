class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # SEE AGAIN -> I didnt do this
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) # if taking +1 or +2 is min

        return min(cost[0], cost[1])