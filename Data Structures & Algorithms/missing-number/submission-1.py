class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        N = len(nums)
        exp = int(N * (N+1) * .5)
        return exp - s
        