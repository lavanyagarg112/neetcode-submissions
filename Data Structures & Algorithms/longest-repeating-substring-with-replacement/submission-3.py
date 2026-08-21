class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = 0

        left = 0
        # chars = set()
        curr_k = k

        # forward pass
        for right in range(len(s)):
            if s[right] != s[left]:
                if curr_k == 0:
                    temp = right
                    curr_k = k
                    while temp > 0:
                        if s[temp - 1] == s[right]:
                            temp -= 1
                        elif curr_k != 0:
                            curr_k -= 1
                            temp -= 1
                        else:
                            break

                    left = temp # reset
                else: # update the character
                    curr_k -= 1
            length = max(length, right - left + 1)

            print(left, right, length, curr_k)

        print(len(s), length, curr_k)
        length += min(len(s) - length, curr_k)

        return length


                    

        