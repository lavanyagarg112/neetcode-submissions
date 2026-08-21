class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # bruteforce

        result = [0, 0]

        def is_palindrome(word):
            return word == word[::-1]

        def helper(s, l, r, result):
            if l < 0 or r >= len(s):
                return

            if s[l] != s[r]:
                helper(s, l+1, r, result)
                helper(s, l, r-1, result)
                return

            if is_palindrome(s[l+1:r]):
                left = result[0]
                right = result[1]
                if (r-l+1) > (right - left + 1):
                    result[0] = l
                    result[1] = r
            return

        helper(s, 0, len(s) - 1, result)

        left = result[0]
        right = result[1]
        return s[left:right+1]
            