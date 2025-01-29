class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]) + 1)] for _ in range(len(obstacleGrid) + 1)]


        dp[1][1] = 1 if obstacleGrid[0][0] != 1 else 0
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if row == 1 and col ==1: continue
                left = dp[row ][col -1 ]
                top =dp[row - 1][col]

                if obstacleGrid[row-1][col-1] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = left + top
        
        print(dp)
        return dp[-1][-1]