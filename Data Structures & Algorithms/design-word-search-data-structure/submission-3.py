class WordDictionary:

    def __init__(self):
        self.start = "#"
        self.dictionary = {"#": set()}
        self.end = "$"
        self.wild = "."

    def canSkip(self, prev_node, word, pos):
        children = self.dictionary[prev_node]
        for ch in children:
            if ch not in self.dictionary:
                continue
            if next_node in self.dictionary[ch]:
                return True

        return False
    
    def searchHelper(self, prefix):

        print(prefix)
        print(self.dictionary)

        node = self.start
        pos = 0

        while pos < len(prefix):
            
            next_node = prefix[pos]

            print(node, next_node)

            if node == self.wild:
                node = next_node
                pos += 1
                continue

            if node not in self.dictionary:
                return node, pos, False
            if next_node not in self.dictionary[node]:
                return node, pos, False
            node = next_node
            pos += 1

        return node, pos, True

    def addWord(self, word: str) -> None:
        
        word = word + self.end
        node, sofarpos, _ = self.searchHelper(word)
        
        for pos in range(sofarpos, len(word)):
            next_node = word[pos]
            if node not in self.dictionary:
                self.dictionary[node] = set()
            if next_node not in self.dictionary[node]:
                self.dictionary[node].add(next_node)
                if next_node != self.end:
                    self.dictionary[node].add(self.wild)
            node = next_node

        return
        

    def search(self, word: str) -> bool:

        word = word + self.end
        _, _, isPresent = self.searchHelper(word)
        return isPresent
        
