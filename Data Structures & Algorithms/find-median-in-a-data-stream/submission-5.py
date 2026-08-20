from heapq import heappush, heapify, heappop

class MedianFinder:

    # keep 2 heaps
    # min and max
    # half and half
    # balance

    def __init__(self):
        self.minLargeheap = []
        self.maxSmallheap = []
        self.minLargeCount = 0
        self.maxSmallCount = 0
        

    def addNum(self, num: int) -> None:
        if self.minLargeheap and num > self.minLargeheap[0]:
            heappush(self.minLargeheap, num)
            self.minLargeCount += 1
        else:
            heappush(self.maxSmallheap, -1 * num)
            self.maxSmallCount += 1

        # balance

        if self.minLargeCount > self.maxSmallCount + 1:
            curr = heappop(self.minLargeheap)
            heappush(self.maxSmallheap, -1 * curr)
            self.maxSmallCount += 1
            self.minLargeCount -= 1
        
        if self.maxSmallCount > self.minLargeCount + 1:
            curr = -1 * heappop(self.maxSmallheap)
            heappush(self.minLargeheap, curr)
            self.minLargeCount += 1
            self.maxSmallCount -= 1


    def findMedian(self) -> float:

        smallHeapVal = 0
        largeHeapVal = 0
        
        if self.maxSmallheap:
            smallHeapVal = -1 * self.maxSmallheap[0]
        if self.minLargeheap:
            largeHeapVal = self.minLargeheap[0]

        if self.maxSmallCount > self.minLargeCount:
            return smallHeapVal

        if self.minLargeCount > self.maxSmallCount:
            return largeHeapVal

        return (smallHeapVal + largeHeapVal)/2.0

        


