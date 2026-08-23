class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = [] # minheap
        freq_map = {}

        for t in tasks:
            if t not in freq_map:
                freq_map[t] = 0
            freq_map[t] += 1

        for t in freq_map:
            heapq.heappush(heap, (-1 * freq_map[t], t))

        excluded = {}
        result = 0

        while heap or excluded:
            result += 1
            # t is a tuple (rem_freq, task)
            to_remove = set()
            for t in excluded:
                if excluded[t] == 0:
                    heapq.heappush(heap, (-1 * t[0], t[1]))
                    to_remove.add(t)
                else:
                    excluded[t] -= 1

            for t in to_remove: 
                excluded.pop(t)

            if not heap:
                continue

            remaining, next_task = heapq.heappop(heap)
            remaining = -1 * remaining
            remaining -= 1
            if remaining > 0:
                excluded[(remaining, next_task)] = n

        return result
