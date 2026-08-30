class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distances = {}
        first = None

        for x1, y1 in points:
            if first == None:
                first = (x1, y1)
            distances[(x1, y1)] = []
            for x2, y2 in points:
                d = abs(x1-x2) + abs(y1-y2)
                if x2 == x1 and y2 == y1:
                    d = float('inf')
                distances[(x1, y1)].append((d, (x2, y2)))

        minCost = 0
        visited = set()

        # diajkstra
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, first))

        while pq:
            current_time, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            print(current_time, node)
            minCost += current_time

            for time, target in distances[node]:
                heapq.heappush(pq, (time, target))

        return minCost
                
