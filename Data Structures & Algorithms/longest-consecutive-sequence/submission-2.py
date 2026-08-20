class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        result = 0

        for n in hashset:
            if n-1 not in hashset: # that is it is a start of a new seq
                curr_length = 1
                curr_num = n
                while curr_num + 1 in hashset:
                    curr_length += 1
                    curr_num += 1
                result = max(curr_length, result)

        return result
        