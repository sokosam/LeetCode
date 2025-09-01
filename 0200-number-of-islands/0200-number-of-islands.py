class Solution:


    def destroyIsland(self, row,col, grid):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "1":
            dirs = [(1,0), (0,1), (-1, 0), (0,-1)]
            grid[row][col] = "0"
            for dx,dy in dirs:
                self.destroyIsland(row + dx, col + dy, grid)
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.destroyIsland(row,col,grid)

                    ans +=1
        return ans
        