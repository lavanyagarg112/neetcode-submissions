class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums)):
            num = nums[i]

            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue # we have already seen this num as starting

            l = i + 1
            r = len(nums) - 1

            while l < r: # cant be = since cant be same index
                threesum = num + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1

                else:
                    result.append([num, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result



