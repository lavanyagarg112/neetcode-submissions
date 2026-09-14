class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        memo = {}

        result = 0  
        result_shift = 0 

        for num2_ind in range(len(num2) - 1, -1, -1):
            num2_dig = num2[num2_ind]
            if num2_dig in memo:
                intermediate = memo[num2_dig]
            else:
                intermediate = 0
                carry = 0
                d2 = mapping[num2_dig]
                power = 0

                for num1_ind in range(len(num1) - 1, -1, -1):
                    num1_dig = num1[num1_ind]
                    d1 = mapping[num1_dig]
                    ans = (d1 * d2) + carry
                    digit = ans % 10
                    print(ans, digit)
                    intermediate = (digit * (10**power)) + intermediate
                    power += 1
                    carry = ans // 10

                intermediate = (carry * (10**power)) + intermediate
                memo[num2_dig] = intermediate

            result += (intermediate * (10 ** result_shift))
            result_shift += 1

        return str(result)
