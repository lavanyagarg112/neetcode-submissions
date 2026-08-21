class Node:

    def __init__(self, val, isEnd=False):
        self.val = val
        # self.children = set()
        self.isEnd = isEnd

    def __eq__(self, other):
        return self.val == other.val

class WordDictionary:

    def __init__(self):
        self.start = "#"
        self.dictionary = {"#": set()}
        self.end = "$"
        self.wild = "."
    
    def searchHelper(self, prefix):

        node = self.start
        
        for pos in range(len(prefix)):
            next_node = prefix[pos]

            if node == self.wild:
                node = next_node
                continue

            if next_node == self.wild:
                node = next_node
                continue

            if node not in self.dictionary:
                return node, pos, False
            if next_node not in self.dictionary[node]:
                return node, pos, False
            node = next_node

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
            node = next_node

        return
        

    def search(self, word: str) -> bool:

        word = word + self.end
        _, _, isPresent = self.searchHelper(word)
        return isPresent
        
