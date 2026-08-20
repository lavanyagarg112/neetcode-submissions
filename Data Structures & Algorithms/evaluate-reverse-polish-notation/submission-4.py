class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]

        result = int(tokens[0]) # given length atleast 1
        # assuming valid inputs

        for i in range(len(tokens)):
            curr = tokens[i]
            if curr in op:
                op2 = stack.pop()
                op1 = stack.pop()
                if curr == "+":
                    result = op1 + op2
                elif curr == "-":
                    result = op1 - op2
                elif curr == "*":
                    result = op1 * op2
                else:
                    if op1 * op2 < 0: # diff signs
                        result = math.ceil(op1/op2)
                        # since they say it goes towards zero
                    else:
                        result = op1//op2
                # print(op1, curr, op2)
                # print(result)
                stack.append(result)

            else:
                stack.append(int(curr))


        return result