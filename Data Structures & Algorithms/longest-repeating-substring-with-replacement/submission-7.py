class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # optimal sliding window
        # keep track of freqeuency of the characters
        # keep track of most frequent character 
            # this is because with the most frequent char
            # we can replace more non-chars using k

        count = {}
        length = 0
        left = 0
        max_f = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_f = max(max_f, count[s[right]]) # max frequency of any character so far

            while (right - left + 1) - max_f > k: # if window size > k + max_frequency need to shrink
                count[s[left]] -= 1 # since we are removing that character
                left += 1

            length = max(length, right - left + 1)

        return length




        