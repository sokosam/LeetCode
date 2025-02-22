class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]) )] for _ in range(len(grid) )]

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                    continue
                up = dp[row -1][col] if row - 1 >= 0 else float('inf')
                left = dp[row][col - 1] if col - 1 >= 0 else float('inf')

                dp[row][col] = min(up + grid[row][col] , left + grid[row][col])


        # for i in dp:
        #     print(i)
        return dp[-1][-1]

