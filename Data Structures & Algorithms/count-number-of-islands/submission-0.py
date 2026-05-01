class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isSafe(x, y):
            if min(x, y) < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            return True

        def dfs(x, y):
            if grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for dx, dy in dirs:
                if isSafe(x + dx, y + dy):
                    dfs(x + dx, y + dy)
            return 

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    res += 1
                    dfs(x, y)
        return res