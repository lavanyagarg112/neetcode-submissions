class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = range(0, len(position))
        stack1 = sorted(cars, key=lambda x:position[x], reverse=True)
        stack2 = [] # new stack
        fleets = 0

        while stack1:
            # print(stack1)
            while stack1:
                c = stack1.pop()
                position[c] += speed[c]
                # position[c] = min(target, position[c])
                stack2.append(c)
            # print(stack2)
            minsofar = float('inf')
            while stack2:
                c = stack2.pop()
                if position[c] >= minsofar:
                    continue
                minsofar = min(position[c], minsofar)
                if position[c] >= target:
                    fleets += 1
                    continue
                stack1.append(c)

        return fleets


