class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefixCols = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for col in range(len(matrix[0])):
            prefix =0 
            for row in range(len(matrix)):
                prefix += matrix[row][col]
                prefixCols[row][col] = prefix
        
        self.area = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for row in range(len(matrix)):
            prefix = 0
            for col in range(len(matrix[0])):
                prefix += prefixCols[row][col]
                self.area[row][col] = prefix
        print(self.area)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = 0
        if row1 - 1 >= 0:
            top = self.area[row1 - 1][col2]
        left = 0
        if col1 - 1 >=0:
            left = self.area[row2][col1 - 1]
        intersect = 0
        
        x,y = min(row1 -1, row2), min(col2, col1 - 1)
        if x >= 0 and y  >= 0:
            intersect = self.area[x][y]
        
        return self.area[row2][col2] - top - left + intersect

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"""


    area = (rowSum + ColSum) - intersect of both

    (4,0)
    (2,3)
    intersect = (2,0)

        (3,1)
        (0,4)

    3   0   1   
    8   6   4
    9   8   4
    13  9   4
    14  9   7

"""

