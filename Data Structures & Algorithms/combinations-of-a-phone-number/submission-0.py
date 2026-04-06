class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numsToLets = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        q = deque()
        q.append('')
        cLen = 0
        while q and cLen != len(digits):
            tmp = len(q)
            for _ in range(tmp):
                curr = q.popleft()
                for i in numsToLets[digits[cLen]]:
                    q.append(curr + i)
            cLen += 1
        return list(q) if len(q) > 1 else []