class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(k):
            res = 0
            for pile in piles:
                res += math.ceil(pile / k)
            if res <= h:
                return True
            return False
        
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            m = (l + r) // 2
            if good(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res