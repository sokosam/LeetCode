class Solution:
    def knightDialer(self, n: int) -> int:
        # dp = [2,2,2,3,0,3,2,2,2,0,2,0]

        adj = [[4,6],[6,8], [7,9], [4,8],[3,9,0], [], [1,7,0],[2,6] ,[1,3], [2,4]]

        dp = [[0 for _ in range(n + 1)]for _ in range(10)]
        # print(dp)

        def makeJump(jumps, curr):
            if jumps == 1:
                return 1

            if dp[curr][jumps] > 0:
                return dp[curr][jumps]
            ans = 0
            print(curr)
            for i in adj[curr]:
                ans += makeJump(jumps - 1, i)
            
            dp[curr][jumps] = ans
            return ans
        
        ans = 0
        for i in range(10):
            ans += makeJump(n, i)
        return ans % (10**9 + 7)