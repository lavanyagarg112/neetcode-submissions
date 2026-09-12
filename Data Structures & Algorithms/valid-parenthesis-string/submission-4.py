class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # ((*)))
        # (((*))

        # hint: two stacks, one for left, one for star

        stackleft = []
        stackstar = []

        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stackleft.append(i)
            elif ch == "*":
                stackstar.append(i)
            else:
                if len(stackleft) != 0:
                    stackleft.pop()
                # here star = left parenthesis
                elif len(stackstar) != 0:
                    stackstar.pop()
                else:
                    return False

        # if more left than star, then def false
        if len(stackleft) > len(stackstar):
            return False

        # hint: have to check for the index of the left and star
        # since now star = right parenthesis
        i = 0
        j = 0
        extras = len(stackstar) - len(stackleft) # some might be empty stars

        while i < len(stackleft):
            leftind = stackleft[i]
            starind = stackstar[i]
            # since it is ordered index already
            if starind < leftind:
                if extras == 0:
                    return False
                extras -= 1
            i += 1
            j += 1

        return True

        

            