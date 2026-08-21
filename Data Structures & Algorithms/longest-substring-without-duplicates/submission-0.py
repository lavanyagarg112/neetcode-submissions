class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # keep the window as long as no duplicate chars
        # as soon as duplicate char, shift the window to after the first occurence of the duplicate char

        # hashmap to store indices
        chars = {}

        left = 0
        right = 0

        length = 0

        while right < len(s) and left <= right:
            if s[right] in chars:
                left = chars[s[right]] + 1 # shift the left pointer
            chars[s[right]] = right
            length = max(length, right - left + 1)
            right += 1

        return length


        