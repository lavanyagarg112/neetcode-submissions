class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def __repr__(self):
        return f"Children: {self.children}, isEnd: {self.isEnd}"


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

        # print(self.root)
        

    def search(self, word: str) -> bool:

        def helper(word, start_node):
            node = start_node
            for i in range(len(word)):
                w = word[i]

                if w == self.wild:
                    if not node.children:
                        return False
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

        
