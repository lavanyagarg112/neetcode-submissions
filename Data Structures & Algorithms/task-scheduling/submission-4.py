class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # using queue makes it faster
        
        heap = [] # minheap
        freq_map = {}

        for t in tasks:
            if t not in freq_map:
                freq_map[t] = 0
            freq_map[t] += 1

        for t in freq_map:
            heapq.heappush(heap, (-1 * freq_map[t], t))

        # excluded = {}
        queue = deque()
        time = 0

        while heap or queue:
            time += 1
            # task is a tuple (rem_freq, task)
            if queue:
                reqtime, task = queue.popleft()
                if reqtime == time:
                    heapq.heappush(heap, (-1 * task[0], task[1]))
                else:
                    queue.appendleft((reqtime, task))

            if not heap:
                continue

            remaining, next_task = heapq.heappop(heap)
            remaining = -1 * remaining
            remaining -= 1
            if remaining > 0:
                queue.append((time + n + 1, (remaining, next_task)))

        return time
