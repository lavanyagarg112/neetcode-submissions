import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place on a specific pos in row x
        # that row, col and diagonal is gone
        # next row
        # if can reach last row -> solution
        # if not -> backtrack

        result = []
        BLOCKED = 1
        OPEN = 0

        board_state = []
        for _ in range(n):
            temp = []
            for _ in range(n):
                temp.append(OPEN)
            board_state.append(temp)

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

            for i in range(n):
                if board_state[row][i] == OPEN:
                    board_state[row][i] = BLOCKED
                    to_unblock = [(row, i)]
                    # col
                    for j in range(n):
                        if board_state[j][i] == OPEN:
                            board_state[j][i] = BLOCKED
                            to_unblock.append((j, i))
                    # row
                    for j in range(n):
                        if board_state[row][j] == OPEN:
                            board_state[row][j] = BLOCKED
                            to_unblock.append((row, j))
                    # diagonal, left, before
                    sub = 1
                    while row - sub >= 0 and i - sub >= 0:
                        if board_state[row-sub][i-sub] == OPEN:
                            board_state[row-sub][i-sub] = BLOCKED
                            to_unblock.append((row-sub, i-sub))
                        sub += 1

                    # diagonal, left, after
                    add = 1
                    while row + add < n and i + add < n:
                        if board_state[row+add][i+add] == OPEN:
                            board_state[row+add][i+add] = BLOCKED
                            to_unblock.append((row+add, i+add))
                        add += 1

                    # diagonal, right, before
                    diff = 1
                    while row - diff >= 0 and i + diff < n:
                        if board_state[row-diff][i+diff] == OPEN:
                            board_state[row-diff][i+diff] = BLOCKED
                            to_unblock.append((row-diff, i+diff))
                        diff += 1

                    # diagonal, right, after
                    diff = 1
                    while row + diff < n and i - diff >= 0:
                        if board_state[row+diff][i-diff] == OPEN:
                            board_state[row+diff][i-diff] = BLOCKED
                            to_unblock.append((row+diff, i-diff))
                        diff += 1

                    pos_set.add((row, i))
                    backtrack(row + 1, pos_set)
                    pos_set.remove((row, i))
                    for r, c in to_unblock:
                        board_state[r][c] = OPEN

        backtrack(0, set())
        return result
