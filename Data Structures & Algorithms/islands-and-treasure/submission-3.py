class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # multisource bfs
        # start from the treasures
        # if reaches the cell first, it is guaranteed to be the shortest

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def process(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            if (r, c) in visited:
                return

            if grid[r][c] == -1:
                return

            visited.add((r, c))
            queue.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        level = 0 # curr distance
        while queue:
            n = len(queue)
            for i in range(n):
                r, c = queue.popleft()
                grid[r][c] = level # the current bfs level
                process(r-1, c)
                process(r+1, c)
                process(r, c-1)
                process(r, c+1)
            level += 1

