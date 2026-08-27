class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currentSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in currentSet:
                currentSet.remove(s[left])
                left += 1
            currentSet.add(s[right])
            result = max(result, right - left + 1)

        return result