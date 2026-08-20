class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0


        for i in range(32):
            if (1 << i) & n: # get bit at that position
                curr = 1
            else:
                curr = 0
            # print(f"curr: {curr:032b}")
            res_intermediate = (res << 1)
            # print(f"resi: {res_intermediate:032b}")
            res = res_intermediate + curr
            # print(f"res: {res:032b}")

        return res
