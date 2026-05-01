class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix) - 1
        c = len(matrix[0])
        #[0, 0] -> len(x), 0 -> len(x), len(y) -> 0, len(y)
        for i in range(len(matrix) // 2):
            matrix[i], matrix[r-i] = matrix[r-i], matrix[i]
        
        for x in range(r+1):
            for y in range(x, c):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
