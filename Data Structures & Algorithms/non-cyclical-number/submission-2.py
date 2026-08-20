class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def square_sum(num):
            res = 0
            while num != 0:
                res += (num % 10) ** 2
                num = num//10

            return res

        while n not in visited:
            visited.add(n)
            curr = square_sum(n) 
            print(curr)
            if curr == 1:
                return True
            n = curr

        return False