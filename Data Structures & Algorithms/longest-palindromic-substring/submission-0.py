class Solution:
    def longestPalindrome(self, s: str) -> str:
        def even(i):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l + 1, s[l:r+1])
        def odd(i):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l + 1, s[l:r+1])
        res, ret = 0, ''
        for i in range(len(s)):
            e, o = even(i), odd(i)
            if e[0] > res:
                ret = e[1]
                res = e[0]
            if o[0] > res:
                ret = o[1]
                res = o[0]
        return ret