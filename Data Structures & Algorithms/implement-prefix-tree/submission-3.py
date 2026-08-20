import string

class PrefixTree:

    def __init__(self):
        self.start = "#"
        self.end = "$"
        self.hashmap = {}
        self.hashmap[self.start] = set()

        # lowercase_alphabets_string = string.ascii_lowercase
        # for ch in lowercase_alphabets_string:
        #     self.hashmap[self.start].add(ch)
        

    def insert(self, word: str) -> None:

        pos, parent = self.trieHelper(word)

        for i in range(pos, len(word)):
            if parent not in self.hashmap:
                self.hashmap[parent] = set()
            if word[i] not in self.hashmap[parent]:
                self.hashmap[parent].add(word[i])
            parent = word[i]

        if parent not in self.hashmap:
            self.hashmap[parent] = set()
        
        if self.end not in self.hashmap[parent]:
            self.hashmap[parent].add(self.end)

        return
        


    def search(self, word: str) -> bool:

        # can naively just add the end char to word and use startsWith

        return self.startsWith(word + self.end)

        
    def trieHelper(self, word: str):

        parent = self.start
        pos = 0

        while parent in self.hashmap and pos < len(word):
            children = self.hashmap[parent]
            if word[pos] in children:
                parent = word[pos]
                pos += 1
            else:
                break

        return pos, parent 

    def startsWith(self, prefix: str) -> bool:

        return self.trieHelper(prefix)[0] == len(prefix)
        
        