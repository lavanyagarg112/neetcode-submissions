class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevmax = 1
        prevmin = 1
        sofar = 1

        result = float("-inf")

        for n in nums:
            sofar *= n
            prevmax = max(prevmax * n, n)
            prevmin = min(prevmin * n, n)

            prevmax = max(prevmax, prevmin)
            prevmin = min(prevmax, prevmin)

            result = max(result, max(sofar, prevmax))

        return result
