class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = defaultdict(int)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def isSafe(x, y):
            return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

        def dp(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            curr = matrix[x][y]
            res = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if isSafe(nx, ny) and matrix[nx][ny] > curr:
                    res = max(res, dp(nx, ny))
            memo[(x, y)] = res + 1
            return memo[(x, y)]
        ret = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                ret = max(ret, dp(x, y))
        return ret