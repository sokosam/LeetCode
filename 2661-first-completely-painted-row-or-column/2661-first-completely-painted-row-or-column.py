class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m = {}
        rowCounts = [len(mat[0])] * len(mat)
        colCounts = [len(mat)] * len(mat[0])

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                m[mat[row][col]] = (row,col)

        print(m)
        print(rowCounts)
        print(colCounts)

        for i in range(len(arr)):
            row , col = m[arr[i]]
            

            rowCounts[row] -=1
            colCounts[col] -=1
            if rowCounts[row] == 0:
                return i
            if colCounts[col] == 0:
                return i
