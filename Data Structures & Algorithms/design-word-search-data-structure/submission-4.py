class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        self.wild = "."
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.isEnd = True
        

    def search(self, word: str) -> bool:

        def helper(word, start_node):
            node = start_node
            for i in range(len(word)):
                w = word[i]
                if node.isEnd:
                    return False

                if w == self.wild:
                    # has children cause not end
                    for ch in node.children:
                        if helper(word[i+1:], node.children[ch]):
                            return True
                    return False

                if w not in node.children:
                    return False
                node = node.children[w]
            return node.isEnd

        return helper(word, self.root)

        
