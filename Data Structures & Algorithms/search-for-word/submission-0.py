class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def helper(board, row, col, word, sofar, path):

            print(row, col, sofar, path)

            if word == sofar:
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if (row, col) in path:
                return False

            sofar = sofar + board[row][col]
            if word.startswith(sofar):
                down = helper(board, row + 1, col, word, sofar, path + [(row, col)])
                up = helper(board, row - 1, col, word, sofar, path + [(row, col)])
                left = helper(board, row, col - 1, word, sofar, path + [(row, col)])
                right = helper(board, row, col + 1, word, sofar, path + [(row, col)])

                return up or down or left or right
            else:
                return False

        starting_indices = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    starting_indices.add((i, j))

        for row, col in starting_indices:
            result = helper(board, row, col, word, "", [])
            if result:
                return True

        return False
