class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)

        def climb(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n <= 2:
                memo[n] = n
                return memo[n]
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        return climb(n)