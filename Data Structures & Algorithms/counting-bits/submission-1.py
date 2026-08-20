class Solution:
    def hammingWeight(self, n: int) -> int:
        nums = list(map(lambda x: x.lstrip("0b"), list(str(bin(n)))))
        count = 0
        for i in nums:
            if i:
                count += 1
        return count
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n+1):
            result.append(self.hammingWeight(i))
        return result
        
        