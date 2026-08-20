class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = range(0, len(position))
        cars = sorted(cars, key=lambda x: position[x], reverse=True)
        times = [] # will be in order of decreasing position
        for c in cars:
            time = (target - position[c])/ speed[c]
            times.append(time)


        fleets = 0
        max_time = float("-inf")

        for t in times:
            if t > max_time: # if i cannot overtake even the car which takes the most time
                fleets += 1
                max_time = max(max_time, t)
        
        return fleets
