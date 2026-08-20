class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # binary search on a matrix

        # probably halving the row and col
        # can also check the first and last of the row

        # oh so binary search row first
        # take the mid row
        # see if first/last is within target
        # if yes then binary search on col
        # otherwise continue binary search on row


        start_r = 0
        end_r = len(matrix) - 1

        start_c = 0
        end_c = len(matrix[0]) - 1

        ans_row = None

        # find row
        while start_r <= end_r:
            mid_r = start_r + (end_r - start_r)//2
            print(mid_r)

            if matrix[mid_r][0] <= target and matrix[mid_r][-1] >= target:
                ans_row = mid_r
                break

            if matrix[mid_r][0] > target:
                end_r = mid_r - 1
            
            if matrix[mid_r][-1] < target:
                start_r = mid_r + 1

        if ans_row == None:
            return False

        while start_c <= end_c:
            mid_c = start_c + (end_c - start_c)//2

            if matrix[ans_row][mid_c] == target:
                return True

            if matrix[ans_row][mid_c] < target:
                start_c = mid_c + 1
            else:
                end_c = mid_c - 1

        return False

