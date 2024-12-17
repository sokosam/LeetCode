class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        maxRow = len(grid) -1 
        maxCol = len(grid[0]) - 1
        def findSize(row,col):
            if row > maxRow or row < 0:
                return 0
            if col > maxCol or col < 0:
                return 0
            if grid[row][col] == 0:
                return 0
            else:
                grid[row][col] = 0
                return findSize(row +1, col) + findSize(row -1, col) + findSize(row, col + 1) + findSize(row, col - 1) + 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    size = findSize(row,col)
                    ans = max(size,ans)
        return ans
