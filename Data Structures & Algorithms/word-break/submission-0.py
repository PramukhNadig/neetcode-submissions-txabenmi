class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return True
            curr = ''
            for j in range(i, len(s)):
                curr += s[j]
                if curr in wordDict:
                    if dp(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dp(0)
                
                
