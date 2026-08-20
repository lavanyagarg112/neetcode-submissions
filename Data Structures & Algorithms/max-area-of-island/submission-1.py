class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        def dfs(r, c): # count curr island

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0

            if (r,c) in visited or grid[r][c] != 1:
                return 0

            visited.add((r, c))
            left = dfs(r-1, c)
            right = dfs(r+1, c)
            top = dfs(r, c-1)
            bottom = dfs(r, c+1)
            return 1 + left + right + top + bottom

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res
            

