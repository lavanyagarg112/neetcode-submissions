class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        m = len(matrix)
        n = len(matrix[0])

        row_start = 0
        row_end = m-1
        col_start = 0
        col_end = n-1

        def is_terminal(rs, re, cs, ce):
            return re < 0 or rs >= m or ce < 0 or cs >= n or (rs > re or cs > ce)

        while True:

            # CHECK TIME AND SPACE
            # AND RECURSIVE SOLUTION

            if is_terminal(row_start, row_end, col_start, col_end):
                break

            top_row = matrix[row_start][col_start: col_end + 1]
            res.extend(top_row)
            row_start += 1

            if is_terminal(row_start, row_end, col_start, col_end):
                break

            right_col = []
            for r in range(row_start, row_end+1):
                right_col.append(matrix[r][col_end])
            res.extend(right_col)
            col_end -= 1

            if is_terminal(row_start, row_end, col_start, col_end):
                break

            down_row = matrix[row_end][col_start: col_end + 1][::-1]
            res.extend(down_row)
            row_end -= 1

            if is_terminal(row_start, row_end, col_start, col_end):
                break

            left_col = []
            for r in range(row_start, row_end+1):
                left_col.append(matrix[r][col_start])
            left_col = left_col[::-1]
            res.extend(left_col)
            col_start += 1

            if is_terminal(row_start, row_end, col_start, col_end):
                break

        return res

