class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def fix(row,col, matrix):
            for i in range(len(matrix)):
                if matrix[i][col] == 0:
                    matrix[i][col] = "True"
                    fix(i,col,matrix)
                matrix[i][col] = "True"
            for i in range(len(matrix[0])):
                if matrix[row][i]== 0:
                    matrix[row][i] = "True"
                    fix(row,i,matrix)
                matrix[row][i] = "True"

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    fix(row,col,matrix)


            

        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "True":
                    matrix[row][col] = 0
        