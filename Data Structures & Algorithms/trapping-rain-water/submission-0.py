class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        rmax, lmax = [0]*N, [0]*N 
        r, l = 0, 0
        for i in range(len(height)):
            r, l = max(r, height[N-(i+1) ]), max(l, height[i])
            rmax[N-(i+1)] = r
            lmax[i] = l
        res = 0 
        for i in range(len(height)):
            res += min(rmax[i], lmax[i]) - height[i]
        return res