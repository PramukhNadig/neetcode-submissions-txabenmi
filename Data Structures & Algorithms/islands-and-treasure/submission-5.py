class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isSafe(row, col):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            if grid[row][col] == -1:
                return False
            return True
        def getMinNeighbors(row, col):
            if grid[row][col] < 1:
                return
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            curr_min = 2147483647
            for addR, addC in dirs:
                if isSafe(row + addR, col + addC):
                    curr_min = min(grid[row + addR][col + addC], curr_min)
            grid[row][col] = curr_min + 1
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                getMinNeighbors(x, y)
        
        for x in range(len(grid) - 1, -1, -1):
            for y in range(len(grid[0]) - 1, -1, -1):
                getMinNeighbors(x, y)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                getMinNeighbors(x, y)
        
        for x in range(len(grid) - 1, -1, -1):
            for y in range(len(grid[0]) - 1, -1, -1):
                getMinNeighbors(x, y)
