class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        reverse_nums = nums[::-1]
        arr1 = [1]
        arr2 = [1]

        temp = 1
        for i in range(1, len(nums)):
            temp = temp * nums[i-1]
            arr1.append(temp)

        temp = 1
        for i in range(1, len(reverse_nums)):
            temp = temp * reverse_nums[i-1]
            arr2.append(temp)

        arr2.reverse()

        result = []

        for i in range(len(nums)):
            result.append(arr1[i] * arr2[i])

        return result