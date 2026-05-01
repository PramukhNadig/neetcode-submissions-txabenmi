class Solution:
    def checkValidString(self, s: str) -> bool:
        # def dp(i, open, close):
        #     if i == len(s):
        #         return open == close
        #     if s[i] == '(':
        #         return dp(i + 1, open + 1, close)
        #     elif s[i] == ')':
        #         if close < open:
        #             return dp(i + 1, open, close + 1)
        #         return False
        #     else:
        #         return dp(i+1, open + 1, close) or dp(i + 1, open, close + 1) or dp(i+1, open, close)
        stars = deque()
        opens = deque()
        for ind, char in enumerate(s):
            if char == '*':
                stars.append(['*', ind])
            elif char == '(':
                opens.append(['(', ind])
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while opens:
            x = -1
            _, i = opens.popleft()
            if not stars:
                return False
            while stars:
                _, x = stars.popleft()
                if x > i:
                    break
            if x < i:
                return False
        return True