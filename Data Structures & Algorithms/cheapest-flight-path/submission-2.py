class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # we can use just diakjstra!

        graph = {}

        for source, dest, price in flights:
            if source not in graph:
                graph[source] = set()
            graph[source].add((price, dest))

        pq = [(0, src, -1)] # -1 stops so far
        heapq.heapify(pq)
        distances = [float('inf')] * n

        while pq:
            cost, node, stops = heapq.heappop(pq)
            if node == dst:
                return cost # we have reached dest
            if stops >= k:
                continue

            for weight, neighbour in graph[node]:
                newcost = cost + weight
                newstops = stops + 1
                if newcost < distances[neighbour]:
                    distances[neighbour] = newcost
                    heapq.heappush(pq, (newcost, neighbour, newstops))

        return -1
