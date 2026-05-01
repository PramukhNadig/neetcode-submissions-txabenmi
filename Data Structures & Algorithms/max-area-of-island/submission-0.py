class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        vis = set()
        def isSafe(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
        def solve(x, y):
            if grid[x][y] == 0:
                return 0
            res = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if isSafe(nx, ny) and (nx, ny) not in vis:
                    vis.add((nx, ny))
                    res += solve(nx, ny)
                    print(res)
            return res
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in vis:
                    vis.add((x, y))
                    res = max(solve(x, y), res)
        return res