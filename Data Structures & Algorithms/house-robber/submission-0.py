class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def f(n):
            if n in memo:
                return memo[n]
            if n >= len(nums):
                return 0
            t = nums[n] + f(n+2)
            dt = f(n+1)
            memo[n] = max(t, dt)
            return max(t, dt)
        return f(0)