class Solution:
    def reverseBits(self, n: int) -> int:
        stack = deque()
        for i in range(32):
            if n & 1:
                stack.append(1)
            else:
                stack.append(0)
            n >>= 1
        res = 0
        exp = 0
        while stack:
            res += 2 ** exp if stack.pop() else 0
            exp += 1
        return res