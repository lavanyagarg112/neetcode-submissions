class Solution:
    def myPow(self, x: float, n: int) -> float:

        res = 1
        isneg = n < 0
        if isneg:
            n = n * -1

        for i in range(n):
            res *= x

        if isneg:
            return 1.0/res

        return res