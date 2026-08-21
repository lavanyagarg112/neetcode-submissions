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

    def canSkip(self, prev_node, next_node):
        children = self.dictionary[prev_node]
        for ch in children:
            if ch not in self.dictionary:
                continue
            if next_node == self.wild:
                if self.end in self.dictionary[ch]:
                    if len(self.dictionary[ch]) > 2:
                        return True
                    else:
                        return False
                else:
                    return True
            if next_node in self.dictionary[ch]:
                return True

        return False
    
    def searchHelper(self, prefix):

        node = self.start
        pos = 0

        while pos < len(prefix):

            next_node = prefix[pos]

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
                self.dictionary[node].add(self.wild)
            node = next_node

        print(self.dictionary)
        return
        

    def search(self, word: str) -> bool:

        word = word + self.end
        _, _, isPresent = self.searchHelper(word)
        return isPresent
        
