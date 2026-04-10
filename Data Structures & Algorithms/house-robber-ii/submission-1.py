class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        if len(nums) ==1:
            return nums[0]
        def dp(i, flag):
            if i == len(nums) - 1 and flag:
                return 0
            if i >= len(nums):
                return 0
            if (i, flag) in memo:
                return memo[(i, flag)]
            w = dp(i + 2, flag) + nums[i]
            wo = dp(i+1, flag)
            memo[(i, flag)] = max(w, wo)
            return max(w, wo)
        
        return max(dp(0, True), dp(1, False))