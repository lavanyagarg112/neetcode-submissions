class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def helper(board, row, col, word, pos, path):

            if pos >= len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if (row, col) in path:
                return False

            if board[row][col] == word[pos]:
                down = helper(board, row + 1, col, word, pos + 1, path + [(row, col)])
                up = helper(board, row - 1, col, word, pos + 1, path + [(row, col)])
                left = helper(board, row, col - 1, word, pos + 1, path + [(row, col)])
                right = helper(board, row, col + 1, word, pos + 1, path + [(row, col)])

                return up or down or left or right
            else:
                return False

        starting_indices = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    starting_indices.add((i, j))

        for row, col in starting_indices:
            result = helper(board, row, col, word, 0, [])
            if result:
                return True

        return False
