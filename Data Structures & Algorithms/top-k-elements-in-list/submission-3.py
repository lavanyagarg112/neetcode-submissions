class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == 0:
            return []

        # bucket sort

        sort_table = [None] * (len(nums) + 1)
        # no need count 0 right by definition
        # but easy to have index0

        freq_table = {}

        for n in nums:
            if n in freq_table:
                # this gives the current count
                count = freq_table[n]
                freq_table[n] += 1
                sort_table[count].remove(n)
                if sort_table[count+1] == None:
                    sort_table[count+1] = []
                sort_table[count+1].append(n)
            else:
                count = 1
                if sort_table[count] == None:
                    sort_table[count] = []
                sort_table[count].append(n)
                freq_table[n] = count 

        result = []
        remaining = k
        for lst in sort_table[::-1]:
            if lst == None:
                continue
            if len(lst) <= remaining:
                result.extend(lst)
                remaining -= len(lst)
            else:
                result.extend(lst[:remaining])
                remaining = 0

            if remaining <= 0:
                break

        return result


        