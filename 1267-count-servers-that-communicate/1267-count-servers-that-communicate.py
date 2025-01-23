class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rowCount = [0 for _ in range(len(grid))]
        colCount = [0 for _ in range(len(grid[0]))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rowCount[row] += 1
                    colCount[col] += 1

        print(rowCount, colCount)
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                ans += 1 if grid[row][col] == 1 and rowCount[row] + colCount[col] -1 >= 2 else 0

        return ans
                