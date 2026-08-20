from heapq import heappush, heapify, heappop

class MedianFinder:

    def __init__(self):
        self.heap = []
        self.count = 0
        self.hasAdded = True
        self.cached = None
        

    def addNum(self, num: int) -> None:
        self.hasAdded = True
        self.count += 1
        heappush(self.heap, num)
        

    def findMedian(self) -> float:
        if not self.hasAdded:
            return self.cached

        med = self.count//2

        temp = []
        for _ in range(med):
            curr = heappop(self.heap)
            temp.append(curr)

        res = heappop(self.heap)
        temp.append(res)
        if self.count % 2 == 0:
            curr = temp[-2] # second last
            res = (res + curr)/2.0
        
        for i in temp:
            heappush(self.heap, i)

        self.cached = res
        self.hasAdded = False
        return res

                

        
        