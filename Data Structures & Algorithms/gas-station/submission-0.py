class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # we want the starting position to have as much 
        # gas as we can fill in

        # so its either the max or none

        if sum(cost) > sum(gas):
            return -1

        maxInd = None
        maxNum = None

        for i in range(len(gas)):

            if maxInd == None:
                if cost[i] <= gas[i]:
                    maxNum = cost[i] - gas[i]
                    maxInd = i
                continue
            if gas[i] - cost[i] > maxNum:
                maxNum = cost[i] - gas[i]
                maxInd = i

        if maxNum == None:
            return -1

        return maxInd
