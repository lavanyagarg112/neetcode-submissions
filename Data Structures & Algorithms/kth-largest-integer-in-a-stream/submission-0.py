class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        

    def add(self, val: int) -> int:
        if val <= self.nums[-1]:
            self.nums.append(val)
        elif val >= self.nums[0]:
            self.nums.insert(0, val)
        else:
            for i in range(len(self.nums)-1):
                if val >= self.nums[i+1] and val <= self.nums[i]:
                    self.nums.insert(i, val)
        return self.nums[self.k-1]
        
