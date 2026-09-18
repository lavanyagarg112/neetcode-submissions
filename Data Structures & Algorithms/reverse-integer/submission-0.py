class Solution:
    def reverse(self, x: int) -> int:
        
        # brute force: convert to string

        # other: construct the rev

        res = 0

        MAX = (2 ** 31) - 1
        MIN = -1 * (2 ** 31)

        temp = x
        res = 0

        while temp:

            '''
            int(a / b)     -> truncates toward 0
            a // b         -> floors toward -infinity
            math.fmod(a,b) -> remainder follows sign of a
            a % b          -> remainder follows sign of b
            '''
            dig = int(math.fmod(temp, 10))
            temp = int(temp/10)

            # check if it will exceed in advance
            if res > MAX/10 or res < MIN/10:
                return 0

            if res == MAX/10 and dig > MAX%10:
                return 0

            if res == MIN/10 and dig < MIN%10:
                return 0

            res = (res * 10) + dig

        return res