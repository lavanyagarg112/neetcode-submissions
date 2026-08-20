class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(nums)):
            target = 0 - nums[i]
            twosum = {}

            for j in range(len(nums)):
                if j == i:
                    continue
                n2 = nums[j]
                if n2 in twosum:
                    # means found a triplet
                    result.append([nums[i], n2, twosum[n2]])
                else:
                    twosum[target - n2] = n2

        # remove duplicates
        visited = set()
        final_result = []

        for indices in result:
            if set(indices) not in visited:
                visited.add(frozenset(indices))
                final_result.append(indices)

        return final_result


        