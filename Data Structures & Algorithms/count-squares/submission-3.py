class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.points:
            self.points[(point[0], point[1])] = 0
        self.points[(point[0], point[1])] += 1
        return
        

    def count(self, point: List[int]) -> int:
        # so anything where the x is on the left/right
        # with a valid y
        # the y is on the top/bottom with valid x
        # and the intersecting point of these two on the other
        # side

        # ahh but mine doesnt check for square

        currx = point[0]
        curry = point[1]

        count = 0

        possible_x_coord = set()
        possible_y_coord = set()

        for x, y in self.points:
            if x == currx and y == curry:
                continue

            if y == curry:
                # one point on x axis
                possible_x_coord.add(x)

            if x == currx:
                possible_y_coord.add(y)

        # if the intersection is there
        for x in possible_x_coord:
            for y in possible_y_coord:
                if (x, y) in self.points:
                    # check for square
                    if abs(x - currx) != abs(y - curry):
                        continue
                    curr_count = self.points[(x, curry)] * self.points[(currx, y)] * self.points[(x, y)]
                    count += curr_count


        return count


        
