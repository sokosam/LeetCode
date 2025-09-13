class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ans = []

        vals = []
        
        for row in range(len(mat)):
            col = 0
            tempRow = row
            temp = []
            while tempRow >= 0 and col >=0 and col < len(mat[0]):
                temp.append(mat[tempRow][col])
                tempRow -=1
                col +=1
            if len(vals) % 2 == 1:
                temp.reverse()
            vals.append(temp)
        
        for col in range(1, len(mat[0])):
            row = len(mat) -1
            tempCol = col
            temp = []
            while row >= 0 and tempCol >=0 and tempCol < len(mat[0]):
                temp.append(mat[row][tempCol])
                row -=1
                tempCol +=1
            if len(vals) % 2 == 1:
                temp.reverse()
            vals.append(temp)
        for i in vals:
            for j in i:
                ans.append(j)
        return ans