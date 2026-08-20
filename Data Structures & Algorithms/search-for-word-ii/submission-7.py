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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        print("hi")
        trie = PrefixTree()
        for w in words:
            trie.insert(w)

        result = set()

        def check_valid(r, c, rows, cols):
            return not (r < 0 or r >= rows or c < 0 or c >= cols)

        def helper(r, c, rows, cols, path, visited, ch, node):

            # print(r, c, path, ch)

            if "".join(path) in words:
                result.add("".join(path))

            if check_valid(r, c-1, rows, cols) and (r, c-1) not in visited and board[r][c-1] in node.children:
                newch = board[r][c-1] 
                helper(r, c-1, rows, cols, path + [newch], visited + [(r, c-1)], newch, node.children[newch])

            if check_valid(r, c+1, rows, cols) and (r, c+1) not in visited and board[r][c+1] in node.children:
                newch = board[r][c+1] 
                helper(r, c+1, rows, cols, path + [newch], visited + [(r, c+1)], newch, node.children[newch])

            if check_valid(r-1, c, rows, cols) and (r-1, c) not in visited and board[r-1][c] in node.children:
                newch = board[r-1][c] 
                helper(r-1, c, rows, cols, path + [newch], visited + [(r-1, c)], newch, node.children[newch])

            if check_valid(r+1, c, rows, cols) and (r+1, c) not in visited and board[r+1][c] in node.children:
                newch = board[r+1][c] 
                helper(r+1, c, rows, cols, path + [newch], visited + [(r+1, c)], newch, node.children[newch])

        root = trie.root
        if not root:
            return []

        chrs = root.children
        # print(chrs)
        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in chrs:
                    helper(r, c, rows, cols, [board[r][c]], [(r, c)], board[r][c], chrs[board[r][c]])


        return list(result)



