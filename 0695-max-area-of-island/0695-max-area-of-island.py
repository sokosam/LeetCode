class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def isWithin(row,col, grid):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

        def getArea(row, col, grid):
            if not isWithin(row,col,grid):
                return 0
            if grid[row][col] == 0:
                return 0
            
            dirs = [(1,0), (0,1) , (-1,0) , (0,-1)]

            ans = 0
            if grid[row][col] == 1:
                ans +=1
                grid[row][col] = 0
            
            for dx,dy in dirs:
                ans += getArea(row + dx, col + dy, grid)
            
            return ans
        
        bestArea = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                bestArea = max(bestArea, getArea( row, col, grid))
        return bestArea