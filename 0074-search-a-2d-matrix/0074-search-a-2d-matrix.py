class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix) - 1
        l = 0
        i = -1
        while l <=r:
            m = l + (r-l)//2
            if matrix[m][0] <= target <= matrix[m][len(matrix[m]) -1]:
                i = m
                break
            elif target < matrix[m][0]:
                r = m -1
            else:
                l = m+ 1
        
        if i == -1:
            return False
        
        r = len(matrix[i]) -1
        l = 0
        while l <=r:
            m = l + (r-l)//2

            if matrix[i][m] == target:
                return True
            elif target < matrix[i][m]:
                r = m - 1
            else:
                l = m + 1
        return False
                
