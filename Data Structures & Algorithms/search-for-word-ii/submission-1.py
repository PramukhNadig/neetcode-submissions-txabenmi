class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = defaultdict() #cannot have this as an optional arg
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode('.')
        res = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isSafe(x, y):
            return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])
        def addWord(word):
            curr = self.root
            for letter in word:
                if letter not in curr.children.keys():
                    curr.children[letter] = TrieNode(letter)
                curr = curr.children[letter]
            curr.isWord = True
        
        for word in words:
            addWord(word)
        
        def solve(x, y, vis, curr, node):
            # print(vis, curr, x, y)
            if node.isWord:
                res.add(curr)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if isSafe(nx, ny) and (nx, ny) not in vis:
                    if board[nx][ny] in node.children:
                        vis.add((nx, ny))
                        solve(nx, ny, vis, curr + board[nx][ny], node.children[board[nx][ny]])
                        vis.remove((nx, ny))
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in self.root.children:
                    vis = set()
                    vis.add((x, y))
                    solve(x, y, vis, ''.join(board[x][y]), self.root.children[board[x][y]])
        
        return list(res)
