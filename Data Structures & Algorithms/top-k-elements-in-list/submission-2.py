from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # heap for getting based on frequency
        # step1: get freq

        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        # step2, add to heap with minimising

        heap = []

        for n, val in freq.items():
            # heappush(heap, (-val, n)) # this is O(nlogn)
            # O(nlogk)
            heappush(heap, (val, n))
            if len(heap) > k:
                heappop(heap)

        # step3: pop from heap

        result = []
        for i in range(k):
            _, n = heappop(heap)
            result.append(n)

        return result

        