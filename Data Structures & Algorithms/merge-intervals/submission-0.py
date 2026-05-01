class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        line = defaultdict(int)
        for x, y in intervals:
            line[x] += 1
            line[y] -= 1
        res = []
        curr = 0
        cIndex = -1
        for key in sorted(line.keys()):
            curr += line[key]
            if cIndex == -1:
                cIndex = key
            if curr == 0:
                res.append([cIndex, key])
                cIndex = -1
        return res