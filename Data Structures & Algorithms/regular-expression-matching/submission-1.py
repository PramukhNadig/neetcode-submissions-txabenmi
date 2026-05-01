class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = defaultdict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j >= len(p):
                return i == len(s)
            if i >= len(s):
                while j < len(p):
                    if j + 1 >= len(p) or p[j+1] != '*':
                        memo[(i, j)] = False
                        return False
                    j += 2
                memo[(i, j)] = True
                return True
            
            if j + 1 < len(p) and p[j + 1] == '*':
                if dp(i, j + 2):
                    memo[(i, j)] = True
                    return True
                curr = p[j]
                for k in range(i, len(s)):
                    if s[k] == curr or curr == '.':
                        if dp(k + 1, j + 2):
                            memo[(i, j)] = True
                            return True
                    else:
                        break
                memo[(i, j)] = False
                return False

            if p[j] == '.' or s[i] == p[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False
        return dp(0, 0)