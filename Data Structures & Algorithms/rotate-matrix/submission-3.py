class Solution: 

    def recurse_rotate(self, matrix, n):

        orig = len(matrix)
        diff = (orig - n)//2
        start = diff
        end = orig - diff

        # base case
        if n <= 1:
            return

        # only look at outer row and col
        leftCol = []
        rightCol = []
        upRow = []
        downRow = []

        for c in range(start, end):
            upRow.append(matrix[start][c])
            downRow.append(matrix[end-1][c])

        for r in range(start, end):
            leftCol.append(matrix[r][start])
            rightCol.append(matrix[r][end-1])
            
        # update
        for r in range(start, end):
            matrix[r][start] = downRow[r-start]
            matrix[r][end-1] = upRow[r-start]

        for c in range(start, end):
            matrix[start][c] = leftCol[end-c-1]
            matrix[end-1][c] = rightCol[end-c-1]

        self.recurse_rotate(matrix, n-2)


    def rotate(self, matrix: List[List[int]]) -> None:
        
        return self.recurse_rotate(matrix, len(matrix))

        

        
        