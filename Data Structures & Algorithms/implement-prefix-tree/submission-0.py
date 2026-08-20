class PrefixTree:

    def __init__(self):
        self.lst = []
        

    def insert(self, word: str) -> None:
        self.lst.append(word)


    def search(self, word: str) -> bool:
        return word in self.lst
        

    def startsWith(self, prefix: str) -> bool:
        for w in self.lst:
            if w.startswith(prefix):
                return True
        return False
        
        