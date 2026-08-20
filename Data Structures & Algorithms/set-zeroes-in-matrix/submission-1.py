class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        FLAG = "Zero"

        for r in range(ROWS):
            curr_row = False
            for c in range(COLS):
                if matrix[r][c] == 0:
                    curr_row = True 
            for c in range(COLS):
                if curr_row:
                    if matrix[r][c] != 0:
                        matrix[r][c] = FLAG

        for c in range(COLS):
            curr_col = False
            for r in range(ROWS):
                if matrix[r][c] == 0:
                    curr_col = True 
            for r in range(ROWS):
                if curr_col:
                    if matrix[r][c] != 0:
                        matrix[r][c] = FLAG
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == FLAG:
                    matrix[r][c] = 0
                    
        