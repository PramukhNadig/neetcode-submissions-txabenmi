class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        t = self.d.get(key)
        if not t:
            return res
        l = 0
        r = len(t) - 1
        def good(m, target):
            if t[m][0] <= target:
                return True
            return False
        while l <= r:
            m = (l + r) // 2
            if good(m, timestamp):
                res = t[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
