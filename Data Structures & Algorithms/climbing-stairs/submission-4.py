class Solution:
    def climbStairs(self, n: int) -> int:
        
        toreachcurr = 1
        toreachprev = 0

        for i in range(n):
            temp = toreachcurr
            toreachcurr = toreachcurr + toreachprev
            toreachprev = temp

        return toreachcurr