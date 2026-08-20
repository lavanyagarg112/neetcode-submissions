class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # keep the window as long as no duplicate chars
        # as soon as duplicate char, shift the window to after the first occurence of the duplicate char

        # hashmap to store indices
        # oh this doesnt work cause we have to remove the prev index characters also
        # best to use set then
        # OHH WE CAN USE HASHMAP
        # JUST MOVE THE LEFT TO BE EITHER TO THAT INDEX OR IF ITS ALR BEYOND THAT
        # KEEP IT THERE

        # q: why is this time O(n)

        chars = {}

        left = 0
        length = 0

        for right in range(len(s)):
            if s[right] in chars:
                left = max(chars[s[right]] + 1, left)
            chars[s[right]] = right
            length = max(length, right - left + 1)

        return length


        