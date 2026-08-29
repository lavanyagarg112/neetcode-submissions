class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # diajkstra?
        # priority queue - heap

        graph = {}

        for source, target, time in times:
            if source not in graph:
                graph[source] = set()
            graph[source].add((target, time))

        pq = []
        heapq.heapify(pq)

        mintime = 0

        heapq.heappush(pq, (0, k))
        visited = set()

        while pq:
            time, source = heapq.heappop(pq)
            if source in visited:
                continue

            mintime += time
            visited.add(source)

            print(source, time)
            if source in graph:
                for target, time in graph[source]:
                    heapq.heappush(pq, (time, target))

        if len(visited) != n:
            return -1
            
        return mintime
        