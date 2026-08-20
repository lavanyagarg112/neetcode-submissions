class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # keep the window as long as no duplicate chars
        # as soon as duplicate char, shift the window to after the first occurence of the duplicate char

        # hashmap to store indices
        # oh this doesnt work cause we have to remove the prev index characters also
        # best to use set then

        # q: why is this time O(n)

        chars = set()

        left = 0
        right = 0

        length = 0

        while right < len(s) and left <= right:
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            length = max(length, right - left + 1)
            right += 1

        return length


        