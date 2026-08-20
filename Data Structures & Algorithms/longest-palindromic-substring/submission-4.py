class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxl = 0
        maxr = 0
        maxlen = 1

        # odd number
        
        for mid in range(len(s)):
            l = mid - 1
            r = mid + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r-l+1) > maxlen:
                        maxl = l
                        maxr = r
                        maxlen = r-l+1
                    l -= 1
                    r += 1
                else:
                    break

        # even number
        
        for mid in range(len(s)):
            mid1 = mid
            mid2 = mid + 1

            if mid2 >= len(s):
                break

            if s[mid1] != s[mid2]:
                continue

            # have to count the two numbers as palindrome
            if maxlen < 2:
                maxl = mid1
                maxr = mid2
                maxlen = 2

            l = mid1 - 1
            r = mid2 + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r-l+1) > maxlen:
                        maxl = l
                        maxr = r
                        maxlen = r-l+1
                    l -= 1
                    r += 1
                else:
                    break

        return s[maxl:maxr+1]



        