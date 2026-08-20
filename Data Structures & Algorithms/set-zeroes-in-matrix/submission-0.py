class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        zerorow = set()
        zerocol = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zerorow.add(r)
                    zerocol.add(c)

        
        for r in range(ROWS):
            for c in range(COLS):
                if r in zerorow or c in zerocol:
                    matrix[r][c] = 0
        