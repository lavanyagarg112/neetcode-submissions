class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # wrong
        # issue: have to ensure that if prev update made it lower, new update makes it faster

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

            min_so_far = min(up, min(down, min(left, right)))
            if min_so_far != INF:
                return min_so_far + 1 # next step is +1 
            else:
                return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    visited = set() # reset
                    grid[r][c] = traverse(r, c) - 1

        return


            
