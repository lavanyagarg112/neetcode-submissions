class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]

        result = int(tokens[0]) # given length atleast 1
        # assuming valid inputs

        for i in range(1, len(tokens)):
            curr = tokens[i]
            if curr in op:
                op2 = stack.pop()
                if curr == "+":
                    result += op2
                elif curr == "-":
                    result -= op2
                elif curr == "*":
                    result *= op2
                else:
                    result /= op2

            else:
                stack.append(int(curr))


        return result