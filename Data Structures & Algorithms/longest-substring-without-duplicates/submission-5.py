class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lastmap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in lastmap:
                left = lastmap[s[right]] + 1
            lastmap[s[right]] = right
            result = max(result, right - left + 1)

        return result