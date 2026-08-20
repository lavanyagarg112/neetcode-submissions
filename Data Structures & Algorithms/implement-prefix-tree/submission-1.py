class PrefixTree:

    def __init__(self):
        self.st = set()
        

    def insert(self, word: str) -> None:
        self.st.add(word)


    def search(self, word: str) -> bool:
        return word in self.st
        

    def startsWith(self, prefix: str) -> bool:
        for w in self.st:
            if w.startswith(prefix):
                return True
        return False
        
        