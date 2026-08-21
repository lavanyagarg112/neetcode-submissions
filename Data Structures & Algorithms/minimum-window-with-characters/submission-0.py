class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        chars = set(t)
        result = ""
        curr_result = ""

        while s[left] not in chars and left < len(s):
            left += 1

        print(left)

        for right in range(left, len(s)):
            if s[right] in t:
                if s[right] in chars:
                    chars.remove(s[right])
                print(s[right], chars)
            curr_result += s[right]
            if len(chars) == 0:
                print(curr_result, left)
                if result == "":
                    result = curr_result
                else:
                    result = min(result, curr_result, key=len)
                chars.add(s[left])
                left += 1
                while s[left] not in t and left < right:
                    print(chars, s[left])
                    left += 1
                curr_result = curr_result[left:]

        return result

                    



        