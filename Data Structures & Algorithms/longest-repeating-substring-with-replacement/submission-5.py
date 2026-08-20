class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        chars = set(s)
        length = 0

        for ch in chars:
            count = 0
            left = 0

            for right in range(len(s)):
                if s[right] == ch:
                    count += 1

                while (right - left + 1) - count > k: # exceeds replacement
                    if s[left] == ch:
                        count -= 1 # since we are removing that character
                    left += 1
                
                length = max(length, right - left + 1)

        return length
        


        




