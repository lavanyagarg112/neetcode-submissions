class Solution:
    def get_int(self, rev_n: str) -> int:
        result = 0
        for i in range(len(rev_n)):
            result += (int(rev_n[i]) * (2 ** i))
        return result    

            
    def reverseBits(self, n: int) -> int:
        part1 = str(bin(n)).lstrip("0b")
        part2 = "0" * (32 - len(part1)) + part1
        return self.get_int(part2)