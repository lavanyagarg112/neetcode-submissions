class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        # odd number
        
        for mid in range(len(s)):
            l = mid - 1
            r = mid + 1

            res += 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
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

            res += 1

            l = mid1 - 1
            r = mid2 + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break

        return res



        