class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i, path):

            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
                
            if (r, c) in path:
                return False

            if board[r][c] != word[i]:
                return False

            path.append((r, c))
            ans = dfs(r-1, c, i+1, path) or dfs(r+1, c, i+1, path) or dfs(r, c-1, i+1, path) or dfs(r, c+1, i+1, path)
            path.pop()
            return ans

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, []):
                        return True

        return False
        

            