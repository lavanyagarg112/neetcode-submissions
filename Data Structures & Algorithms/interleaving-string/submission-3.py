class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # three strings -> s1, s2, s3
        # s1 interleave s2 -> s3
        # the diff between number of substrings from s1 and s2 is atmost 1
        # IMPORTANT: this is automatically satisfied by interleaving 
        # BECAUSE we take stuff alternatively so it will alwaysss work outtttt
        # there cannot be any situation where this diff is more than one
        # because if two substrings from the same string is consecutive then that is ONE substring
        # need to use all chars. order cannot change

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        # s1: i, s2: j, s3: k

        def dp(i, j):
            
            k = i + j # IMP

            if (i, j) in memo:
                return memo[(i, j)]

            if k >= len(s3): # we have exhausted all s1 and s2 and reached end of s3
                return True

            ans = False
            if i < len(s1) and s3[k] == s1[i]:
                ans = ans or dp(i+1, j)
            
            if j < len(s2) and s3[k] == s2[j]:
                ans = ans or dp(i, j+1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

            

            


        