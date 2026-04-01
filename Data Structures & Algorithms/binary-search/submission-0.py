class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def good(p, target):
            if nums[p] >= target:
                return True
            else:
                return False
        
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if good(m, target):
                r = m - 1
                res = m
            else:
                l = m + 1

        return res if nums[res] == target else -1