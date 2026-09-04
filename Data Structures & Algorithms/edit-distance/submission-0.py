class Solution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:

        if (word1, word2) in self.memo: # this could also just use index
            return self.memo[(word1, word2)]
        
        if word1 == word2:
            return 0

        if len(word1) == 0:
            return len(word2) # add remaining chars

        if len(word2) == 0:
            return len(word1) # delete remaining chars

        curr1 = word1[0]
        curr2 = word2[0]

        if curr1 == curr2:
            ans = self.minDistance(word1[1:], word2[1:])
        else:
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            delete = 1 + self.minDistance(word1[1:], word2)
            add = 1 + self.minDistance(word1, word2[1:])
            ans = min(replace, min(delete, add))

        self.memo[(word1, word2)] = ans
        return ans

        