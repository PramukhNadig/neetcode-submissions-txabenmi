class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = set()
        def dfs(x, y):

            if x >= len(board) or y >= len(board[0]):
                return
            if min(x, y) < 0:
                return 
            if board[x][y] == 'X':
                return
            board[x][y] = 'T'
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in vis:
                    vis.add((nx, ny))
                    dfs(nx, ny)
            return
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # for x in range(1, len(board) - 1):
        #     for y in range(1, len(board[0]) - 1):
        #         if board[x][y] == 'O':
        #             board[x][y] = 'T'
        for x in range(len(board)):
            if board[x][0] == 'O':
                dfs(x, 0)
            if board[x][len(board[0]) - 1] == 'O':
                dfs(x, len(board[0]) - 1)
        for y in range(len(board[0])):
            if board[0][y] == 'O':
                dfs(0, y)
            if board[len(board) - 1][y] == 'O':
                dfs(len(board) - 1, y)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                if board[x][y] == 'T':
                    board[x][y] = 'O'

        
