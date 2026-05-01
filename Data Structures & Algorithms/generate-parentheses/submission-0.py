class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen(open, close, s):
            if close == open == n:
                res.append(s)
                return
            if close < open:
                gen(open, close + 1, s + ')')
            if open < n:
                gen(open + 1, close, s + '(')
            if open < close:
                return
        gen(0, 0, '')
        return res



        