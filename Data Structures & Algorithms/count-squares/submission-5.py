class CountSquares:

    # optimisation for count to be O(n)

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        # O(1)
        if (point[0], point[1]) not in self.points:
            self.points[(point[0], point[1])] = 0
        self.points[(point[0], point[1])] += 1
        return
        

    def count(self, point: List[int]) -> int:
        # O(n^2)
        # so anything where the x is on the left/right
        # with a valid y
        # the y is on the top/bottom with valid x
        # and the intersecting point of these two on the other
        # side

        currx = point[0]
        curry = point[1]

        count = 0

        for (x, y) in self.points:
            # check for square
            # check if it is a potential diagonal
            if abs(x - currx) != abs(y - curry) or x == currx or y == curry:
                continue
            if (x, curry) not in self.points or (currx, y) not in self.points:
                continue
            curr_count = self.points[(x, curry)] * self.points[(currx, y)] * self.points[(x, y)]
            count += curr_count


        return count


        
