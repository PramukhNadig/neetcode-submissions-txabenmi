class Solution:
    def search(self, nums: List[int], target) -> int:
        l, r = 0, len(nums) - 1
        
        def good(l, m, r, target):
            if nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    return False
                else:
                    return True
            else:
                if target >= nums[m] and target <= nums[r]:
                    return True
                else:
                    return False
        res = -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if good(l, m, r, target):
                l = m + 1
            else:
                r = m - 1

        return -1