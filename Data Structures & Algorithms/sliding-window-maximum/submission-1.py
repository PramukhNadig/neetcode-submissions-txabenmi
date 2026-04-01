class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = [0]*len(nums)
        for i in range(len(nums)):
            if q and i-k >= q[0][1]:
                q.popleft()
            while q and (nums[i] >= q[-1][0]):
                q.pop()
            q.append([nums[i], i])
            res[i] = q[0][0]
        # print(res)
        return res[k-1:]