class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1
        if n % 25 != 0 and n != 0:
            n += 25
        amt = n//25 + 1 

        dp = [[ [-1,-1,-1] for _ in range(0, n//25  + 1)] for _ in range(n//25 + 1)]
        # if n % 25 == 0 and n != 0:
        #     dp.pop()
        #     for row in dp:
        #         row.pop()

        for col in range(len(dp)):
            dp[0][col] = [0,1,0]
        for row in range(len(dp)):
            dp[row][0] = [1,0,0]
        dp[0][0] = [0,0,1]
        # print(dp)

        def helper(a,b):
            nonlocal dp
            
            if dp[a//25 ][b//25 ] != [-1,-1,-1]:
                return dp[a//25][b//25]
            
            p1 = helper(max(a - 100,0), b)
            p2 = helper(max(a - 75,0), max(b - 25,0))
            p3 = helper(max(a - 50,0), max(b - 50,0))
            p4 = helper(max(a - 25,0), max(b - 75,0))

            aWins = 0.25*(p1[0] + p2[0] + p3[0] + p4[0])
            bWins = 0.25*(p1[1] + p2[1] + p3[1] + p4[1])
            cWins = 0.25*(p1[2] + p2[2] + p3[2] + p4[2])



            dp[a//25][b//25] = [aWins, bWins, cWins]
            return dp[a//25][b//25]
        helper(n,n)
        return 1 -( dp[-1][-1][0] + 0.5*dp[-1][-1][2])

        """




        [[[0, 0, 1], [0, 1, 0], [0, 1, 0]],
        [[1, 0, 0], [-1, -1, -1], [-1, -1, -1]],
        [[1, 0, 0], [-1, -1, -1], [0.25, 0.5, 0.25]]]
        """