import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place on a specific pos in row x
        # that row, col and diagonal is gone
        # next row
        # if can reach last row -> solution
        # if not -> backtrack

        # time: O(n^2 * n!)
        # n! -> row 0: n choices, row 1: n-1 choices ..
        # n^2 -> for each iteration, two for loops
        # space: O(n^2) -> rec: O(n), pos_state: O(n) = O(n) + O(n), solution construction: O(n^2)


        result = []
        pos_set = set()
        visitedcol = set()
        posDiag = set()
        negDiag = set()

        def backtrack(row):
            if row == n:
                res = []
                for r in range(n):
                    temp = ""
                    for c in range(n):
                        if (r,c) in pos_set:
                            temp += "Q"
                        else:
                            temp += "."
                    res.append(temp)
                result.append(res)
                return

            for col in range(n):
                if col in visitedcol or (row + col) in posDiag or (row-col) in negDiag:
                    continue
                visitedcol.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                pos_set.add((row, col))
                backtrack(row + 1)
                pos_set.remove((row, col))
                negDiag.remove(row-col)
                posDiag.remove(row+col)
                visitedcol.remove(col)

        backtrack(0)
        return result
