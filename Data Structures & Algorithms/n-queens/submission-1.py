import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place on a specific pos in row x
        # that row, col and diagonal is gone
        # next row
        # if can reach last row -> solution
        # if not -> backtrack

        result = []
        # BLOCKED = 1
        # OPEN = 0

        # board_state = []
        # for _ in range(n):
        #     temp = []
        #     for _ in range(n):
        #         temp.append(OPEN)
        #     board_state.append(temp)

        def backtrack(row, pos_set):
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
                # it can never be in same row since we are going
                # row by row
                CONSIDER = True
                for r, c in pos_set: # if its in col or diagonal
                    if col == c or abs(row-r) == abs(col-c):
                        CONSIDER = False
                        break
                if not CONSIDER:
                    continue
                pos_set.add((row, col))
                backtrack(row + 1, pos_set)
                pos_set.remove((row, col))

        backtrack(0, set())
        return result
