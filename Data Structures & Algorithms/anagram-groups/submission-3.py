class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_frequency_table(string):
            table = [0] * 26
            for s in string:
                ind = ord(s) - ord('a')
                table[ind] += 1

            return str(table)

        result_table = {}
        for s in strs:
            freq = get_frequency_table(s)
            if freq in result_table:
                result_table[freq].append(s)
            else:
                result_table[freq] = [s]

        result = []

        for rt in result_table:
            result.append(result_table[rt])

        return result

        