class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # brute force

        res = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > curr:
                    res.append(j-i)
                    break
            else:
                res.append(0)

        return res