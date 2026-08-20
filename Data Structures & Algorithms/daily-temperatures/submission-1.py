class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # stack
        # idea: store until we get a num that is larger
        # and keep popping until a larger number comes
        # and for the indices that we pop, we add the 
        # curr - that ind
        # since it means that the indices we pop
        # are smaller and were in decreasing order


        stack = [0]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            print(stack)
            while len(stack) > 0 and curr > temperatures[stack[-1]]:
                rem = stack.pop()
                res[rem] = i-rem
                print(i, res)
            stack.append(i)

        return res


        
            