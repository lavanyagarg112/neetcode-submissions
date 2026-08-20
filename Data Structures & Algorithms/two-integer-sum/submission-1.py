class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary to keep track of what is done
        # and what is the next target


        dictionary = {}

        for i in range(len(nums)):
            n = nums[i]
            if n in dictionary:
                return [dictionary[n], i]
            else:
                dictionary[target - n] = i # store the target

        return [0,0]
        