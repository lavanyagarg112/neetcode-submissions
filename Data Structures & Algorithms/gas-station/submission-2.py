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

            # print(i, maxInd, maxNum)

            if maxInd == None:
                if cost[i] <= gas[i]:
                    maxNum = gas[i] - cost[i]
                    maxInd = i
            else:
                if gas[i] - cost[i] > maxNum:
                    maxNum = gas[i] - cost[i]
                    maxInd = i
            # print(i, maxInd, maxNum)

        if maxNum == None:
            return -1

        return maxInd
