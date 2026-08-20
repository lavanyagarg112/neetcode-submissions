class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = None 

            if num-1 in hash_table:
                hash_table[num-1] = num
            
            if num+1 in hash_table:
                hash_table[num] = num+1

        # identify longest seq
        result = 0
        temp_count = 0
        curr_num = min(hash_table)

        while hash_table:
            curr_num = hash_table.pop(curr_num)
            temp_count += 1
            result = max(result, temp_count)
            if curr_num == None and hash_table:
                temp_count = 0
                curr_num = min(hash_table)

        return result
        