class Solution:

    def __init__(self):
        self.memo = {}

    def numDecodings(self, s: str) -> int:

        if s in self.memo:
            return self.memo[s]

        if not s:
            return 1
        
        if s.startswith("0"):
            return 0

        res = 0
        if int(s[0]) >= 1 and int(s[0]) <= 26:
            res += self.numDecodings(s[1:])

        if len(s) > 1 and int(s[0:2]) >= 1 and int(s[0:2]) <= 26:
            res += self.numDecodings(s[2:])

        self.memo[s] = res
        return res

        