class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # gas[i] - cost[i] >= 0
        # brute force: try every starting point as starting point
        # greedy
        # if at any point the total cost is < 0
        # restart from next station, since by starting 
        # at any station upto then, it will 
        # always give neg too since we start with an empty tank
        # so if from station 1 -> 4 then at 4 its neg
        # then even if we start at station 2 with 0, where before 
        # we started at station 2 with >= 0 since station 1 could have had some left
        # so then at station 4 even then it will hit neg

        if sum(gas) < sum(cost):
            return -1


        start = 0
        while start < len(gas):
            # path = list(range(start, len(gas))) + list(range(0, start + 1))
            curr = 0
            # why does it work without path??? - TO CHECK
            for dest in range(start, len(gas)):
                curr += (gas[dest] - cost[dest])
                if curr < 0:
                    start = dest + 1
                    break

            if curr >= 0:
                return start

        return -1