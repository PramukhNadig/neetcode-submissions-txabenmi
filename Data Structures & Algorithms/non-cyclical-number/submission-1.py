class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        def s(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res
        def go(n):
            if n == 1:
                return True
            if n in vis:
                return False
            vis.add(n)
            j = s(n)
            return go(j)
        return go(n)