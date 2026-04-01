class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def good(row, col, target):
            if matrix[row][col] > target:
                return True
            else:
                return False
        
        rowL, rowR = 0, len(matrix) - 1
        r = -1
        while rowL <= rowR:
            m = (rowL + rowR) // 2
            if good(m, 0, target):
                rowR = m - 1
            else:
                rowL = m + 1
                r = m

        colL, colR = 0, len(matrix[0]) - 1
        c = -1
        while colL <= colR:
            m = (colL + colR) // 2
            if good(r, m, target):
                colR = m - 1
            else:
                colL = m + 1
                c = m 
        return matrix[r][c] == target