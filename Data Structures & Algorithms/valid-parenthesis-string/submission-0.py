class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # ((*)))
        # (((*))

        # hint: two stacks, one for left, one for right

        stackleft = []
        stackstar = []

        for ch in s:
            if ch == "(":
                stackleft.append(ch)
            elif ch == "*":
                stackstar.append(ch)
            else:
                if len(stackleft) != 0:
                    stackleft.pop()
                elif len(stackstar) != 0:
                    stackstar.pop()
                else:
                    return False

        return len(stackleft) <= len(stackstar)

            