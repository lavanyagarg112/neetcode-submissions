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
            current_time, source = heapq.heappop(pq)
            if source in visited:
                continue

            mintime = current_time # since signals can reach two places at the same time
            visited.add(source)

            if source in graph:
                for target, time in graph[source]:
                    heapq.heappush(pq, (current_time + time, target))

        if len(visited) != n:
            return -1
            
        return mintime
        