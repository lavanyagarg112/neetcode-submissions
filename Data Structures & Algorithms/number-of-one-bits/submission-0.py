class Solution:
    def hammingWeight(self, n: int) -> int:
        nums = list(map(lambda x: x.lstrip("0b"), list(str(bin(n)))))
        count = 0
        for i in nums:
            if i:
                count += 1
        return count