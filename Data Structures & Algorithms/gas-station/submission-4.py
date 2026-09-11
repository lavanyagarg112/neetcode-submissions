class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # gas[i] - cost[i] >= 0
        # brute force: try every starting point as starting point

        if sum(gas) < sum(cost):
            return -1


        for start in range(len(gas)):
            path = list(range(start, len(gas))) + list(range(0, start + 1))
            curr = 0
            for dest in path:
                curr += (gas[dest] - cost[dest])
                if curr < 0:
                    break

            if curr >= 0:
                return start

        return -1