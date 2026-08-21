class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        neg = None
        pos = None
        maxsofar = float("-inf")

        for n in nums:
            if n < 0:
                if neg == None:
                    if pos != None:
                        neg = n * pos
                        pos = 1
                    else:
                        neg = n
                    maxsofar = max(maxsofar, neg)
                elif pos == None:
                    pos = neg * n
                    neg = n
                    maxsofar = max(maxsofar, max(pos, neg))
                else:
                    neg, pos = pos * n, neg * n
                    maxsofar = max(maxsofar, max(pos, neg))
            else:
                if pos == None:
                    pos = n
                    if neg != None:
                        neg = n * neg
                    maxsofar = max(maxsofar, pos)
                elif neg == None:
                    pos = pos * n
                    maxsofar = max(maxsofar, pos)
                else:
                    neg, pos = neg * n, pos * n
                    maxsofar = max(maxsofar, max(pos, neg))

            maxsofar = max(maxsofar, n)

        return maxsofar
                