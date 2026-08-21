class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2**31 - 1
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def traverse(r, c):
            # return dist

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return INF

            if grid[r][c] == -1:
                return INF

            if grid[r][c] != INF:
                return grid[r][c] + 1

            if (r,c) in visited:
                return INF

            visited.add((r, c))

            up = traverse(r-1, c)
            down = traverse(r+1, c)
            left = traverse(r, c-1)
            right = traverse(r, c+1)

            grid[r][c] = min(up, min(down, min(left, right)))
            if grid[r][c] != INF:
                return grid[r][c] + 1 # next step is +1 
            else:
                return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    visited = set() # reset
                    traverse(r, c)

        return


            
