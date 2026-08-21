class Solution:

    def __init__(self):
        self.separator = "%separator%"

    def encode(self, strs: List[str]) -> str:
        return (self.separator).join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.separator)
