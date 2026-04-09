class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        i = 1
        curr = intervals[0]
        res = 0
        while i < len(intervals):
            while i < len(intervals) and curr[1] > intervals[i][0]:
                i += 1
                res += 1
            if i < len(intervals):
                curr = intervals[i]
            i += 1
        return res