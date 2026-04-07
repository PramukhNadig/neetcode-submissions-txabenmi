class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpos, maxneg = nums[0], nums[0]
        res = nums[0]
        for num in nums[1:]:
            maxpos, maxneg = max(maxpos * num, maxneg * num, num), min(maxneg * num, maxpos * num, num)
            res = max(res, maxpos)
        return res