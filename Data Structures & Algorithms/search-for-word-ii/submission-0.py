class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = set()
        
        def backtrack(word, pos, path, row, col):

            if pos == len(word):
                res.add(word)
                return

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return

            if (row, col) in path:
                return

            curr = word[pos]
            if board[row][col] != curr:
                return

            backtrack(word, pos+1, path + [(row, col)], row + 1, col)
            backtrack(word, pos+1, path + [(row, col)], row - 1, col)
            backtrack(word, pos+1, path + [(row, col)], row, col+1)
            backtrack(word, pos+1, path + [(row, col)], row, col-1)

        word_start = {}

        for w in words:
            ch = w[0]
            if ch not in word_start:
                word_start[ch] = set()
            word_start[ch].add(w)

        for r in range(len(board)):
            for c in range(len(board[r])):
                ch = board[r][c]
                if ch in word_start:
                    curr_words = word_start[ch]
                    for cw in curr_words:
                        backtrack(cw, 0, [], r, c)

        return list(res)


            

            

            