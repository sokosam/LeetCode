class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, n//2) if i*i < n]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for square in squares:
            for x in range(square, n + 1):
                dp[x] = min(dp[x] , dp[x - square]  +1)
        return dp[n] if dp[n] != float('inf') else -1 