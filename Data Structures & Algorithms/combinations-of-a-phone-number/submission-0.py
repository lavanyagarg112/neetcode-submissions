class Solution:

    def __init__(self):
        self.mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
        "7": "pqrs", "8": "tuv", "9": "wxyz"}
        

    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        if len(digits) == 1:
            return list(self.mapping[digits[0]])
            
        curr = list(self.mapping[digits[0]])
        future = self.letterCombinations(digits[1:])
        result = []
        for f in future:
            for c in curr:
                result.append(c + f)  

        return result                  


        