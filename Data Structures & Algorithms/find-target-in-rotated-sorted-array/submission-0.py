class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start)//2)

            if nums[mid] == target:
                return mid

            if nums[-1] < nums[mid]:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    if nums[0] > target:
                        start = mid + 1
                    else:
                        end = mid - 1

            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    if nums[-1] < target:
                        end = mid - 1
                    else:
                        start = mid + 1

        return -1




        