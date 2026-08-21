class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {"{": "}", "(": ")", "[": "]"}

        for br in s:
            if br in brackets:
                stack.append(br)
            else:
                if len(s) > 0:
                    prev = stack.pop()
                    if brackets[prev] != br:
                        return False
                else:
                    return False

        return len(stack) == 0
        