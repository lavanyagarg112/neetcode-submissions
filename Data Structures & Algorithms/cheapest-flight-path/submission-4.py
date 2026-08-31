class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # we can use just diakjstra!
        # oh but need additional dimension to see HOW MANY STOPS SO FAR

        graph = {}

        for source, dest, price in flights:
            if source not in graph:
                graph[source] = set()
            graph[source].add((price, dest))

        pq = [(0, src, 0)] # 0 flights used so far
        heapq.heapify(pq)
        # dist[node][flights_used]
        distances = [[float('inf')] * (k + 2) for _ in range(n)]

        while pq:
            cost, node, flights = heapq.heappop(pq)
            if node == dst:
                return cost # we have reached dest
            if flights >= k + 1:
                continue
            if cost > distances[node][flights]:
                continue

            if node in graph:
                for weight, neighbour in graph[node]:
                    newcost = cost + weight
                    newflights = flights + 1
                    if newflights > k + 1:
                        continue
                    if newcost < distances[neighbour][newflights]:
                        distances[neighbour][newflights] = newcost
                        heapq.heappush(pq, (newcost, neighbour, newflights))

        return -1
