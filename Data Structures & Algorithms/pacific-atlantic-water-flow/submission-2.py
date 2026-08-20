class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, path, prev):
            if (r, c) in path:
                return

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            # why less than? shouldnt it be < in path
            # oh cause here we are going uphill
            # trying to find which cells are REACHABLE to pacific/atlantic
            if heights[r][c] < prev:
                return

            path.add((r, c))
            dfs(r + 1, c, path, heights[r][c])
            dfs(r - 1, c, path, heights[r][c])
            dfs(r, c + 1, path, heights[r][c])
            dfs(r, c - 1, path, heights[r][c])

        # first and last row
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r,c) in atlantic:
                    result.append([r, c])

        return result
