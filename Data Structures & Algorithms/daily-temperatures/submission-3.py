class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # dynamic programming
        # backwards
        # if next then 1
        # else 


        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    break 
                j += res[j]
            else:
                res[i] = j-i

        return res