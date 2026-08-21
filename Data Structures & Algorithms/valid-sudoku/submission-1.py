class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = 9
        cols = 9
        # check rows
        for row in range(rows):
            visited = set()
            for col in range(cols):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in visited:
                    return False
                else:
                    if int(board[row][col]) not in range(1,10):
                        return False
                    visited.add(board[row][col])

        # check cols
        for col in range(cols):
            visited = set()
            for row in range(row):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in visited:
                    return False
                else:
                    if int(board[row][col]) not in range(1,10):
                        return False
                    visited.add(board[row][col])

        # make sub boxes
        visited = set()
        for row in range(3):
            for col in range(3):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)
        visited = set()
        for row in range(3):
            for col in range(3,6):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)

        visited = set()
        for row in range(3):
            for col in range(6,9):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)

        visited = set()
        for row in range(3,6):
            for col in range(3):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)
        visited = set()
        for row in range(3,6):
            for col in range(3,6):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)

        visited = set()
        for row in range(3,6):
            for col in range(6,9):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)

        visited = set()
        for row in range(6,9):
            for col in range(3):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)
        visited = set()
        for row in range(6,9):
            for col in range(3,6):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)

        visited = set()
        for row in range(6,9):
            for col in range(6,9):
                curr = board[row][col]
                if curr == '.':
                    continue
                elif curr in visited:
                    return False
                else:
                    if int(curr) not in range(1,10):
                        return False
                    visited.add(curr)

        
        return True

            


            


        