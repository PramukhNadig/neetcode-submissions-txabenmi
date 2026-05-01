class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i >= len(prices):
                return 0
            if i in memo:
                return memo[i]
            wo = dp(i + 1)
            curr = prices[i]
            res = 0
            for j in range(i + 1, len(prices)):
                if prices[j] > curr:
                    res = max(res, prices[j] - curr + dp(j + 2))
            
            memo[i] = max(res, wo)
            return memo[i]
        res = 0
        for i in range(len(prices)):
            res = max(res, dp(i))
        # print(memo)
        return res