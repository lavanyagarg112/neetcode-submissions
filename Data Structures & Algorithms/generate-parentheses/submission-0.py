class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # again backtracking
        result = []

        def backtrack(n_open, n_close, order):
            if n_open == 0 and n_close == 0:
                result.append(order)
                return

            if n_open == 0:
                order += (")" * n_close)
                result.append(order)
                return

            # invalid cases:
            # n_close = 0 and n_open != 0
            # n_open > n_close i.e. there are more open left than closed

            backtrack(n_open - 1, n_close, order + "(")
            if n_open < n_close:
                backtrack(n_open, n_close - 1, order + ")")

            return

        backtrack(n, n, "")
        return result