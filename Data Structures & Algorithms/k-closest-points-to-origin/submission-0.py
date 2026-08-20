class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x, y):
            return math.sqrt((x * x) + (y * y))
        
        heap = []
        heapq.heapify(heap)

        while points:
            x, y = points.pop()
            dist = distance(x, y)
            heapq.heappush(heap, (-1 * dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _, p in heap:
            x, y = p
            result.append([x, y])

        return result



