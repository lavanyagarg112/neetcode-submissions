class Node:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def __repr__(self):
        return f"Children: {self.children}, isEnd: {self.isEnd}"

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True

    def getLongestWords(self):
        res = []

        def helper(node, path):

            if not node.children:
                res.append("".join(path))
                return

            for ch in node.children:
                helper(node.children[ch], path + [ch])
        
        helper(self.root, [])
        return res
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        prefixtree = PrefixTree()
        for word in set(words):
            prefixtree.insert(word)
        # prefixtree.insert("a")
        # for ch in prefixtree.root.children:
        #     print(ch)
        # print("***")
        starting_chars = prefixtree.root.children

        res = []

        def backtrack(node, row, col, path, visited):


            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return

            if (row, col) in visited:
                return

            if path[-1] != board[row][col]:
                return

            if node.isEnd:
                print("end!")
                # means we have found a word so far
                res.append("".join(path))
                # but there may be more so we dont end

            for ch in node.children:
                curr_node = node.children[ch]

                backtrack(curr_node, row+1, col, path + [ch], visited + [(row, col)])
                backtrack(curr_node, row-1, col, path + [ch], visited + [(row, col)])
                backtrack(curr_node, row, col+1, path + [ch], visited + [(row, col)])
                backtrack(curr_node, row, col-1, path + [ch], visited + [(row, col)])
            
            return
                    
        for r in range(len(board)):
            for c in range(len(board[r])):
                ch = board[r][c]
                if ch in starting_chars:
                    backtrack(starting_chars[ch], r, c, [ch], [])

        return res



        