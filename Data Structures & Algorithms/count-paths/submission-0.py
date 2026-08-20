class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}

        def recurs(i, j):

            if i > m-1 or j > n-1:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if (i,j) in memo:
                return memo[(i, j)]

            ans = recurs(i+1, j) + recurs(i, j+1) 

            # print(i, j, ans)
            
            memo[(i, j)] = ans
            return ans

        return recurs(0, 0)

            

        

