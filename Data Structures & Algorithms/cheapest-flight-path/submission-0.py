class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = {}

        for source, dest, price in flights:
            if source not in graph:
                graph[source] = set()
            graph[source].add((price, dest))

        k_hops_graph = {}

        queue = deque()
        
        # bfs on k levels

        level = 0
        queue.append(src) # the input
        k_hops_graph[src] = set()

        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                node = queue.popleft()
                if level > k:
                    break
                if node in graph:
                    for price, dest in graph[node]:
                        k_hops_graph[node].add((price, dest))
                        if dest not in k_hops_graph:
                            k_hops_graph[dest] = set()
                        queue.append(dest)
            if level > k:
                break
            level += 1

        # k hops graph is what we can do diajkstra on now

        pq = [(0, src)]
        distances = [float('inf')] * n
        distances[src] = 0
        visited = set()

        heapq.heapify(pq)

        while pq:
            cost, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)

            for nextcost, nextnode in k_hops_graph[node]:
                newcost = nextcost + distances[node]

                if newcost < distances[nextnode]:
                    distances[nextnode] = newcost
                    heapq.heappush(pq, (newcost, nextnode))

        if distances[dst] == float('inf'):
            return -1
        return distances[dst]
