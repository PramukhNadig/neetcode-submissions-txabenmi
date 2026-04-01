class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res, ret = 10 ** 20, ''
        N = len(s)
        c = Counter(t)
        tC = Counter()
        matches = len(c.keys())

        for r in range(len(s)):
            tC[s[r]] += 1
            if tC[s[r]] == c[s[r]]:
                matches -= 1
            while matches == 0:
                if (r - l + 1) < res:
                    res = r - l + 1
                    ret = s[l:r+1]
                tC[s[l]] -= 1
                if tC[s[l]] == (c[s[l]] - 1):
                    matches += 1
                l += 1
        return ret