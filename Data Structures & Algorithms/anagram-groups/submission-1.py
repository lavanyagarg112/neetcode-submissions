class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_frequency_table(string):
            table = {}
            for s in string:
                if s not in table:
                    table[s] = 0
                table[s] += 1

            return table

        result_table = {}
        for s in strs:
            freq = frozenset(get_frequency_table(s))
            if freq in result_table:
                result_table[freq].append(s)
            else:
                result_table[freq] = [s]

        result = []

        for rt in result_table:
            result.append(result_table[rt])

        return result

        