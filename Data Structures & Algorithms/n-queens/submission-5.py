import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place on a specific pos in row x
        # that row, col and diagonal is gone
        # next row
        # if can reach last row -> solution
        # if not -> backtrack

        # time: O(n * n!)
        # n! -> row 0: n choices, row 1: n-1 choices ..
        # n -> for each iteration, one for loop
        # space: O(n^2) -> rec: O(n), pos_state: O(n) = O(n) + O(n), solution construction: O(n^2)


        result = []
        queens = []
        visitedcol = set()
        posDiag = set()
        negDiag = set()

        def backtrack(row):
            if row == n:
                res = []
                for col in queens:
                    res.append("." * col + "Q" + "." * (n-col-1))
                result.append(res)
                return

            for col in range(n):
                if col in visitedcol or (row + col) in posDiag or (row-col) in negDiag:
                    continue
                visitedcol.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                queens.append(col)

                backtrack(row + 1)

                queens.pop()
                negDiag.remove(row-col)
                posDiag.remove(row+col)
                visitedcol.remove(col)

        backtrack(0)
        return result
