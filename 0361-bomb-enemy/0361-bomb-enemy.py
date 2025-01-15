class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        dp = [[0 for _ in range(len(grid[0]))]for _ in range(len(grid)) ] 
        dp2 = [[0 for _ in range(len(grid[0]))]for _ in range(len(grid)) ] 
        def checkRow(curr, row, col):
            if col < 0:
                return 0
            if grid[row][col] == "W":
                checkRow(0,row, col - 1)
                return 0
            elif grid[row][col] == "E":
                curr += 1
                val = max(checkRow(curr , row, col -1),curr)
                dp[row][col] = val
                return val
            else:
                val = max(checkRow(curr, row, col -1),curr)
                dp[row][col] = val
                return val

        def checkCol(curr, row, col):
            if row < 0:
                return 0
            if grid[row][col] == "W":
                checkCol(0,row - 1, col)
                return 0
            elif grid[row][col] == "E":
                curr += 1
                val = max(checkCol(curr , row - 1, col),curr)
                dp2[row][col] = val
                return val
            else:
                val = max(checkCol(curr, row - 1, col),curr)
                dp2[row][col] = val
                return val

        for row in range(len(grid)):
            checkRow(0,row,len(grid[0]) - 1)

        for col in range(len(grid[0])):
            checkCol(0,len(grid) - 1, col)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    ans = max(dp[row][col] + dp2[row][col], ans)

        return ans