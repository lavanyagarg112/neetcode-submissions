class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            currset = set()
            currd = {}

            for i in s:
                if i in currd:
                    currd[i] += 1
                else:
                    currd[i] = 1

            for key in currd:
                value = currd[key]
                currset.add((key, value))

            finalset = frozenset(currset)

            if finalset in anagrams:
                anagrams[finalset].append(s)
            else:
                anagrams[finalset] = [s]

        result = []
        for key in anagrams:
            result.append(anagrams[key])

        return result

