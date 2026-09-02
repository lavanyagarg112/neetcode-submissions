class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        
        # top down

        memo = {}

        def recurse(a, i):
            if a == 0: # can do!
                return 1

            if i >= len(coins): # cannot do
                return 0

            if (a, i) in memo:
                return memo[(a, i)]

            curr = coins[i]
            include = 0
            if a >= curr:
                include = recurse(a - curr, i)
            exclude = recurse(a, i+1)
            ans = include + exclude

            memo[(a, i)] = ans
            return ans

        return recurse(amount, 0)

        