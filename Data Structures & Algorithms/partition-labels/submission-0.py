class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        beginnings = defaultdict()
        ends = defaultdict()
        for ind, val in enumerate(s):
            ends[val] = ind
        
        res = []
        last = -1
        currMax = 0
        for ind, val in enumerate(s):
            if ends[val] > currMax:
                currMax = ends[val]
            if currMax == ind:
                res.append(currMax - last)
                currMax = ind + 1
                last = ind
        return res
