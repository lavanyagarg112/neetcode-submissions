class MinStack:

    # one stack 
    # idea: store the diff of the curr val and prev min
    # update the curr min
    # SEE AGAIN

    def __init__(self):
        self.stack = []
        self.currmin = None
        

    def push(self, val: int) -> None:

        if len(self.stack) == 0:
            self.stack.append(0)
            self.currmin = val
        else:
            diff = val - self.currmin
            self.stack.append(diff)
            self.currmin = min(self.currmin, val)
        

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr < 0:
            # the current min is the val
            self.currmin = self.currmin - curr
        

    def top(self) -> int:
        curr = self.stack[-1]
        if curr > 0:
            return self.currmin + curr
        else:
            return self.currmin
        

    def getMin(self) -> int:
        return self.currmin
        
