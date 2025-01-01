class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroes.append((row,col))

        def fix(row,col, matrix):
            for i in range(len(matrix)):
                matrix[i][col] = 0
            
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        
        for zero in zeroes:
            fix(zero[0], zero[1], matrix)
        