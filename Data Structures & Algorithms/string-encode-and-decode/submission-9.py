class Solution:

    # this can be easily bypassed
    # we need something that by definition cant be bypassed

    def __init__(self):
        # self.separator = "%separator%"
        # use unicode instead
        self.separator = "\u2764"
        self.isEmpty = "\U0001F40D"

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return self.isEmpty
        encoded = (self.separator).join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == self.isEmpty:
            return []
        decoded = s.split(self.separator)
        return decoded
