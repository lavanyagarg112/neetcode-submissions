class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_height = max(height)

        width = 0
        total = 0

        for h in range(1, max_height + 1):
            first = None
            ind = 0
            width = 0
            while ind < len(height):
                if height[ind] >= h:
                    first = ind
                    break
                ind += 1
            else:
                continue

            for i in range(first + 1, len(height)):
                if height[i] < h:
                    width += 1
                else:
                    total += width
                    width = 0

        return total