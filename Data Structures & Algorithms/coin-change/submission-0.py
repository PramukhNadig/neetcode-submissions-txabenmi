class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        INF = 10 ** 20
        memo = defaultdict()
        def dp(amt, i):
            if (amt, i) in memo:
                return memo[(amt, i)]
            if amt < 0:
                return INF
            if amt == 0:
                return 0
            if i >= len(coins):
                return INF
            take = dp(amt - coins[i], i) + 1
            dont = dp(amt, i + 1)
            memo[(amt, i)] = min(take, dont)
            return min(take, dont)
        res = dp(amount, 0)
        if res == INF:
            return -1
        return res