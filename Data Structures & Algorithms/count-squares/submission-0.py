class CountSquares:

    def __init__(self):
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        return
        

    def count(self, point: List[int]) -> int:
        # so anything where the x is on the left/right
        # with a valid y
        # the y is on the top/bottom with valid x
        # and the intersecting point of these two on the other
        # side

        currx = point[0]
        curry = point[1]

        count = 0

        possible_x_coord = []
        possible_y_coord = []

        for x, y in self.points:
            if x == currx and y == curry:
                continue

            if y == curry:
                # one point on x axis
                possible_x_coord.append(x)

            if x == currx:
                possible_y_coord.append(y)

        # if the intersection is there
        for x in possible_x_coord:
            for y in possible_y_coord:
                if [x, y] in self.points:
                    count += 1


        return count


        
