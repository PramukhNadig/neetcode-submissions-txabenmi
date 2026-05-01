class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict()
        M, N = m - 1, n - 1
        def dp(x, y):
            if (x, y) == (M, N):
                return 1
            if (x, y) in memo:
                return memo[(x, y)]
            res = 0
            if x != M:
                res += dp(x + 1, y)
            if y != N:
                res += dp(x, y + 1)
            memo[(x, y)] = res
            return res

        return dp(0, 0)