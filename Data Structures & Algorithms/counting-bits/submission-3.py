class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # why do the time complexities say O(nlogn)
        # shouldnt it be O(n^2)

        # and shouldnt the below be O(n)
        return [bin(i).count('1') for i in range(n + 1)]