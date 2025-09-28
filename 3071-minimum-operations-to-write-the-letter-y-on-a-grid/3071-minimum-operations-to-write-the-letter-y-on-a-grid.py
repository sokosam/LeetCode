class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        
        yNums = [0,0,0]
        allElse = [0,0,0]

        halfPoint = len(grid)//2
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == col and col <= halfPoint:
                    yNums[grid[row][col]] +=1
                elif row + col == len(grid) -1 and row <= halfPoint:
                    yNums[grid[row][col]] +=1
                elif row > halfPoint and col == halfPoint:
                    yNums[grid[row][col]] +=1
                else:
                    allElse[grid[row][col]] +=1
        


        totalY = sum(yNums)
        totalAll = sum(allElse)
        best = float('inf')
        for i in range(len(yNums)):
            changeY = totalY - yNums[i]
            for j in range(len(allElse)):
                if i == j:
                    continue
                changeAll = totalAll - allElse[j]
                best = min(best, changeY + changeAll)
        return best 
