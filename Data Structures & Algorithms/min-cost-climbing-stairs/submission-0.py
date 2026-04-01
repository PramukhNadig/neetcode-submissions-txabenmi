class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        def climb(n):
            if n in memo:
                return memo[n]
            if n >= len(cost):
                return 0
            
            memo[n] = cost[n] + min(climb(n+1), climb(n+2))
            return memo[n]
        return min(climb(0), climb(1))