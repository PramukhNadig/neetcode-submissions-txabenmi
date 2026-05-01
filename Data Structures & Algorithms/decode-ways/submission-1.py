class Solution:
    def numDecodings(self, s: str) -> int:
        memo = defaultdict()
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            num = int(s[i])
            if num >= 3:
                memo[i] = dp(i+1)
                return memo[i]
            if num == 0:
                return 0
            if num == 1:
                if i != len(s) - 1:
                    memo[i] = dp(i + 1) + dp(i + 2)
                    return memo[i]
                else:
                    memo[i] = dp(i+1)
                    return memo[i]
            if num == 2:
                if i != len(s) - 1 and int(s[i+1]) < 7:
                    memo[i] = dp(i + 1) + dp(i + 2)
                    return memo[i]
                else:
                    memo[i] = dp(i+1)
                    return memo[i]
            return 0
        return dp(0)

        