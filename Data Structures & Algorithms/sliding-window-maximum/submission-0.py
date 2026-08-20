class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []

        curr_max = max(nums[:k])
        is_first = False
        if curr_max == nums[0]:
            is_first = True
        output.append(curr_max)

        left = 0

        for right in range(k, len(nums)):
            left += 1
            if not is_first:
                if nums[right] >= curr_max:
                    curr_max = nums[right]
                    is_first = False
                else:
                    # curr max remains same
                    if nums[left] == curr_max:
                        is_first = True
                    else:
                        is_first = False

            else:
                if nums[right] >= curr_max:
                    curr_max = nums[right]
                    is_first = False
                else:
                    curr_max = max(nums[left:right+1])
                    if nums[left] == curr_max:
                        is_first = True
                    else:
                        is_first = False
            
            output.append(curr_max)

        return output

            
