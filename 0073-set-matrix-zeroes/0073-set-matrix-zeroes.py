class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        setRow = -1
        setCol = -1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    if setRow == -1:
                        setRow = row
                        setCol = col
                    matrix[setRow][col] = 0
                    matrix[row][setCol] = 0
        if setRow == -1:
            return    

        for col in range(len(matrix[setRow])):
            if matrix[setRow][col] == 0 and col != setCol:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        for row in range(len(matrix)):
            if matrix[row][setCol] == 0 and row != setRow:
                for col in range(len(matrix[setRow])):
                    matrix[row][col] = 0

        for col in range(len(matrix[setRow])):
            matrix[setRow][col]= 0
        for row in range(len(matrix)):
            matrix[row][setCol]= 0      
        