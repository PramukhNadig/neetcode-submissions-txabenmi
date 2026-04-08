class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def isSafe(x, y):
            return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])
        
        def dfs(x, y, i, vis):
            if (x, y) in vis:
                return False
            if board[x][y] != word[i]:
                return False
            vis.add((x, y))
            if i == len(word) - 1:
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in vis and isSafe(nx, ny):
                    if dfs(nx, ny, i + 1, vis):
                        return True
            vis.remove((x, y))
            return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x, y, 0, set((x, y))):
                    return True
        return False