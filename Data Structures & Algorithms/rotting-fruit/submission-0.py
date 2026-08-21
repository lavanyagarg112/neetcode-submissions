class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        level = 0
        queue = deque()
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: # if rotten
                    queue.append((r, c))
                    visited.add((r, c))

        def process(r, c):
            if r < 0 or c < 0 or r >= rows or c >= rows:
                return

            if (r, c) in visited:
                return

            if grid[r][c] == 0:
                return

            grid[r][c] = 2
            queue.append((r, c))
            visited.add((r, c))

        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                process(r-1, c)
                process(r+1, c)
                process(r, c-1)
                process(r, c+1)
            level += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # if fresh
                    return -1

        return level - 1 # since we start with minute 0
