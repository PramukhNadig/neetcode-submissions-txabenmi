"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line = Counter()
        for i in range(len(intervals)):
            s, e = intervals[i].start, intervals[i].end
            line[s] += 1
            line[e] -= 1
        res, curr = 0, 0
        for i in sorted(line.keys()):
            curr += line[i]
            res = max(res, curr)
        return res