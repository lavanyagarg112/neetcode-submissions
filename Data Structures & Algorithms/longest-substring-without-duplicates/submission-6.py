class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lastmap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in lastmap:
                # max with left cause if we are alr past 
                # the last occurent then we dont care
                left = max(lastmap[s[right]] + 1, left)
            lastmap[s[right]] = right
            result = max(result, right - left + 1)

        return result