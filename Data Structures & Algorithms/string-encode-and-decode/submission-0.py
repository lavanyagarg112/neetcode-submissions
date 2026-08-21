class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s + "#"
        return result
            

    def decode(self, s: str) -> List[str]:
        result = s.split("#")
        return list(filter(lambda x: x != "", result))
