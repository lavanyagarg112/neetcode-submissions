class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        
        def dfs(s):

            if not s:
                return True

            if s in memo:
                return memo[s]

            for w in wordDict:
                if s.startswith(w):
                    if dfs(s[len(w):]):
                        memo[s] = True
                        return True

            memo[s] = False
            return False

        return dfs(s)