class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = list(set(coins))
        coins.sort(reverse=True)

        memo = defaultdict(int)
        def dp(i, amt):
            if amt < 0:
                return 0
            if amt == 0:
                return 1
            if (i, amt) in memo:
                return memo[(i, amt)]
            if i == len(coins):
                return 0
            w, wo = dp(i, amt - coins[i]), dp(i+1, amt)
            memo[(i, amt)] = w + wo
            return w + wo
        
        return dp(0, amount)