class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = 0
        prev_length = 0

        left = 0
        curr_k = k

        # forward pass
        for right in range(len(s)):
            if s[right] != s[left]:
                if curr_k == 0: # go to last occurence
                    temp = right
                    curr_k = k
                    while temp > 0 and s[temp - 1] == s[right]:
                        temp -= 1
                    left = temp # reset
                else: # update the character
                    curr_k -= 1
            prev_length = right - left + 1
            length = max(length, prev_length)

            print(left, right, length, curr_k)

        print(len(s), length, curr_k)
        length = max(length, prev_length + min(len(s) - prev_length, curr_k))

        return length


                    

        