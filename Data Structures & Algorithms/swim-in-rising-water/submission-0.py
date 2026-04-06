class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:        
        heap = [(grid[0][0], 0, 0)]          
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        vis = set()
        #after processing, add to vis

        def isSafe(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

        while heap:
            cMax, x, y = heapq.heappop(heap)
            if x == R - 1 and y == C - 1:
                return cMax

            if (x, y) in vis:
                continue
            vis.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if isSafe(nx, ny):
                    heapq.heappush(heap, [max(cMax, grid[nx][ny]), nx, ny])
        return -1
                