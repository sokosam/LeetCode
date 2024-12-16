class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        maxRows = len(grid) -1 
        maxCols = len(grid[0]) - 1

        def destroyIsland(row, col):
            if row > maxRows or row < 0:
                return
            if col > maxCols or col < 0:
                return
            if grid[row][col] != '1':
                return
            else:
                grid[row][col] = '0'
                destroyIsland(row + 1, col)
                destroyIsland(row -1, col)
                destroyIsland(row , col -1)
                destroyIsland(row, col + 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    destroyIsland(row,col)
                    count +=1
        return count