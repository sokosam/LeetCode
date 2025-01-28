class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        
        # dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        total = 0

        for row in grid:
            for col in row:
                if col > 0:
                    total += col

        
        def dfs(row, col, arr):
            

            dirs = [(0,1), (1,0), (-1,0), (0,-1)]
            
            arr[0] += grid[row][col]
            arr[1] +=1
            grid[row][col] = -1
            for dx, dy in dirs:
                if   row + dx >= 0 and row + dx < len(grid) and col + dy >= 0 and col +dy < len(grid) and grid[row+ dx][col + dy] >= 0:
                    dfs(row + dx, col +dy , arr)
                
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1:
                    continue

                arr = [0,0]
                dfs(row, col, arr)
                ans += (total - arr[0]) * arr[1]
                # dirs = [(0,1), (1,0), (-1,0), (0,-1)]
                # for dx,dy in dirs:
                #     if row + dx >= 0 and row + dx < len(grid) and col + dy >= 0 and col +dy < len(grid) and dp[row+ dx][col + dy] > 0:
                #         dp[row][col] = dp[row+dx][col +dy]
                #         break
                # if dp[row][col] > 0:
                #     ans += dp[row][col]
                #     continue
                # else:
                #     dp[row][col] = total - dfs(row, col)
                #     ans += dp[row][col]
                
        # ans =0
        # for row in dp:
        #     for col in row:
        #         ans += col
        return ans


