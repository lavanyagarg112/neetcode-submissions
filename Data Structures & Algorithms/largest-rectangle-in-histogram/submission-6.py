class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # O(n) space and time
        # from solution: monotonic stack

        n = len(heights)

        stack = []
        left = [-1] * n
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() # get the max it can expand to the left
            if stack:
                left[i] = stack[-1] # top
            stack.append(i) # we dont care about the ones we popped
            # cause if the ones popped > i
            # and i > curr
            # then the ones popped > curr, so they would
            # always get popped

        stack = []
        right = [n] * n

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            stack.append(i)

        
        res = 0

        for i in range(n):
            left[i] += 1 # start from the index not smaller
            right[i] -= 1 # end at the index not smaller
            area = heights[i] * (right[i] - left[i] + 1)
            res = max(res, area)

        return res

