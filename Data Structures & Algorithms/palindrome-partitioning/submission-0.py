class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def is_palindrome(string):
            return string == string[::-1]

        def backtrack(i, path):

            if path and not is_palindrome(path[-1]):
                return

            if i == len(s):
                result.append(path[::])
                return
            
            init = i
            while i < len(s):
                path.append(s[init:i+1])
                backtrack(i+1, path)
                path.pop()
                i += 1

        backtrack(0, [])
        return result
