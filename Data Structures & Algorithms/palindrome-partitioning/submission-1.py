class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def is_palindrome(string):
            return string == string[::-1]

        def backtrack(i, path):

            if i == len(s):
                result.append(path[::])
                return
            
            init = i
            while i < len(s):
                word = s[init:i+1]
                if is_palindrome(word):
                    path.append(word)
                    backtrack(i+1, path)
                    path.pop()
                i += 1

        backtrack(0, [])
        return result
