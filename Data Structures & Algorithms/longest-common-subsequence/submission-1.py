class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}

        def recurs(i, j, length):
            print(i, j, length)
            if i == len(text1) and j == len(text2):
                return length

            if i >= len(text1) or j >= len(text2):
                return length

            if (i, j) in memo:
                return max(length, memo[(i, j)])

            ans = length
            if text1[i] == text2[j]:
                ans = max(ans, recurs(i+1, j+1, length+1))
            else:
                tempans = max(recurs(i+1, j, length), recurs(i, j+1, length))
                ans = max(ans, tempans)
            memo[(i, j)] = ans
            return ans

        res = recurs(0, 0, 0)
        print(memo)
        return res