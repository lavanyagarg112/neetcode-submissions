class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # using iterative dfs
        
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c, convert):
            stack = [(r,c)]

            while stack:
                r, c = stack.pop()
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    return

                if (r, c) in visited:
                    return

                visited.add((r, c))
                if board[r][c] == "O":
                    board[r][c] = convert
                    stack.append((r-1, c))
                    stack.append((r+1, c))
                    stack.append((r, c+1))
                    stack.append((r, c-1))
        
        # first visit all the Os from the edges

        # rows
        for r in [0, rows-1]:
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == "O":
                    dfs(r, c, "EDGE")

        # cols
        for r in range(rows):
            for c in [0, cols-1]:
                if (r,c) not in visited and board[r][c] == "O":
                    dfs(r, c, "EDGE")

        # then visit the ones not from the edges and convert them
        for r in range(rows-1):
            for c in range(cols-1):
                if (r,c) not in visited and board[r][c] == "O":
                    dfs(r, c, "X")

        # then convert EDGE back to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "EDGE":
                    board[r][c] = "O"

        return