class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # O(nlogn) time
        # O(n) space
        
        heap = []
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, -1 * s)

        while len(heap) >= 2:
            max1 = -1 * heapq.heappop(heap)
            max2 = -1 * heapq.heappop(heap)
            rem = abs(max1 - max2)
            if rem != 0:
                heapq.heappush(heap, -1 * rem)

        if len(heap) == 1:
            return -1 * heapq.heappop(heap)
        else:
            return 0
