class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        subgrids = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for r in range(len(board)):
            rows.append(set())
            curr_r = rows[r]
            for c in range(len(board[0])):
                if len(cols) <= c:
                    cols.append(set())

                curr_c = cols[c]
                curr = board[r][c]

                if curr == ".":
                    continue

                curr_grid = None
                if r < 3:
                    if c < 3:
                        curr_grid = subgrids[0]
                    elif c < 6:
                        curr_grid = subgrids[1]
                    else:
                        curr_grid = subgrids[2]
                elif r < 6:
                    if c < 3:
                        curr_grid = subgrids[3]
                    elif c < 6:
                        curr_grid = subgrids[4]
                    else:
                        curr_grid = subgrids[5]
                else:
                    if c < 3:
                        curr_grid = subgrids[6]
                    elif c < 6:
                        curr_grid = subgrids[7]
                    else:
                        curr_grid = subgrids[8]

                if int(curr) < 1 or int(curr) > 9:
                    return False

                if curr in curr_r or curr in curr_c or curr in curr_grid:
                    return False

                curr_r.add(curr)
                curr_c.add(curr)
                curr_grid.add(curr)

        return True
