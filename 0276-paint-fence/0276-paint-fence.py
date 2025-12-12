class Solution:
    def numWays(self, n: int, k: int) -> int:
        


        dp= [-1]*(n + 3)
        dp[1] = k
        dp[2] = k*k

        def bt(n,k):
            if dp[n] > 0:
                return dp[n]
            

            dp[n] = (bt(n -1,k)+bt(n-2,k))*(k-1)
            return dp[n]

        return bt(n,k)