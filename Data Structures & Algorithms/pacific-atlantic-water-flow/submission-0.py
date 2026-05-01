class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pac, atl = set(), set()

        def isSafe(x, y):
            if x >= len(heights) or y >= len(heights[0]):
                return False
            if min(x, y) < 0:
                return False
            return True

        def dfs(x, y, s):
            if (x, y) in s:
                return
            s.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if isSafe(nx, ny) and heights[x][y] <= heights[nx][ny] and (nx, ny) not in s:
                    dfs(nx, ny, s)
            
            return
        
        for x in range(len(heights)):
            dfs(x, 0, pac)
            dfs(x, len(heights[0]) - 1, atl)
        
        for y in range(len(heights[0])):
            dfs(0, y, pac)
            dfs(len(heights) - 1, y, atl)

        return list(pac.intersection(atl))