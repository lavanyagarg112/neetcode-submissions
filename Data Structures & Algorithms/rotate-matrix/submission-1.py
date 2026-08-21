class Solution: 

    def recurse_rotate(self, matrix, n):

        orig = len(matrix)
        diff = (orig - n)//2
        print(n, matrix)

        # base case
        if n <= 1:
            return

        # only look at outer row and col
        leftCol = []
        rightCol = []
        upRow = []
        downRow = []

        for c in range(diff, n+diff):
            upRow.append(matrix[diff][c])
            downRow.append(matrix[n+diff-1][c])

        for r in range(diff, n+diff):
            leftCol.append(matrix[r][diff])
            rightCol.append(matrix[r][n+diff-1])

        print(leftCol, rightCol, upRow, downRow)
        # update
        for r in range(diff, n+diff):
            matrix[r][diff] = downRow[r-diff]
            matrix[r][n+diff-1] = upRow[r-diff]

        for c in range(diff, n+diff):
            matrix[diff][c] = leftCol[n-c-1-diff]
            matrix[n+diff-1][c] = rightCol[n-c-1-diff]

        self.recurse_rotate(matrix, n-2)


    def rotate(self, matrix: List[List[int]]) -> None:
        
        return self.recurse_rotate(matrix, len(matrix))

        

        
        