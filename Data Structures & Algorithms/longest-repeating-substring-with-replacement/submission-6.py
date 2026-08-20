class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # optimal sliding window
        # keep track of freqeuency of the characters

        count = {}
        length = 0
        left = 0
        max_f = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_f = max(max_f, count[s[right]])

            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)

        return length




        