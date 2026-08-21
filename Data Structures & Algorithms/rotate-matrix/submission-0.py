class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)

        # base case
        if n <= 1:
            return

        n = len(matrix)

        # only look at outer row and col
        leftCol = []
        rightCol = []
        upRow = []
        downRow = []

        for c in range(n):
            upRow.append(matrix[0][c])
            downRow.append(matrix[n-1][c])

        for r in range(n):
            leftCol.append(matrix[r][0])
            rightCol.append(matrix[r][n-1])


        # update
        for r in range(n):
            matrix[r][0] = downRow[r]
            matrix[r][n-1] = upRow[r]

        for c in range(n):
            matrix[0][c] = leftCol[n-c-1]
            matrix[n-1][c] = rightCol[n-c-1]


        n = len(matrix)
        self.rotate(matrix[1:n-1][1:n-1])

        
        