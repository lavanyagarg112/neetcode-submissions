class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        ans = float('inf')

        while start <= end:
            mid = start + ((end - start) // 2)
            ans = min(ans, nums[mid])

            print(start, end, mid, ans)

            if nums[-1] < nums[mid]:
                start = mid + 1

            else:
                end = mid - 1

        return ans


            

