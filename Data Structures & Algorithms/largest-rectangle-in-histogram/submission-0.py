class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        res = 0
        N = len(heights)
        for ind, val in enumerate(heights):
            lastpop = ind
            while stack and val < stack[-1][0]:
                res = max(res, stack[-1][0] * (ind - stack[-1][-1]))
                lastpop = stack[-1][1]
                stack.pop()
                
            stack.append([val, lastpop])

        
        for val, ind in stack:
            res = max(res, val * (N-ind))
        return res