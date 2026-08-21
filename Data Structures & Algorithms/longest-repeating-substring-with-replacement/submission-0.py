class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = 0

        left = 0
        chars = {}
        curr_k = k

        # forward pass
        for right in range(len(s)):
            if s[right] != s[left]:
                if curr_k == 0:
                    if s[right] in chars:
                        left = max(chars[s[right]], left) # move left pointer to first occurence
                    else:
                        left = right # reset
                        curr_k = k
                else: # update the character
                    curr_k -= 1
            
            chars[s[right]] = right
            length = max(length, right - left + 1)

        right = len(s) - 1
        chars = {}
        curr_k = k

        # back pass
        for left in range(len(s)-1, -1, -1):
            if s[left] != s[right]:
                if curr_k == 0:
                    if s[left] in chars:
                        right = min(chars[s[left]], right)
                    else:
                        right = left
                        curr_k = k
                else:
                    curr_k -= 1
            chars[s[left]] = left
            length = max(length, right - left + 1)

        return length


                    

        