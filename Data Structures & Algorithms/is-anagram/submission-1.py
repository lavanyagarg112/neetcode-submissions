class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency table
        # not O(1) space
                
        def get_freq_table(string):
            table = {}
            for s in string:
                if s in table:
                    table[s] += 1
                else:
                    table[s] = 1
            return table

        return get_freq_table(s) == get_freq_table(t)