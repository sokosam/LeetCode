class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        n*m*m
        """
        dp = [[0 for _ in range(len(points[0]))] for _ in range(len(points) + 1)]
        for rindex, row in enumerate(points):
            curr = 0
            # print(dp)
            for dpindex, i in enumerate(dp[rindex]):
                if dpindex == 0:
                    curr = i
                    continue
                curr -=1 
                curr = max(curr, i)
                dp[rindex][dpindex] = curr
            # print(dp)


            curr = 0
            for dpindex in range(len(dp[rindex]) - 1, -1 ,-1):
                if dpindex == len(dp[rindex]) - 1:
                    curr = dp[rindex][dpindex]
                    continue
                curr -=1 
                curr = max(curr, dp[rindex][dpindex])
                dp[rindex][dpindex] = curr
            # print(dp)
            for cindex, col in enumerate(row):
                dp[rindex + 1][cindex] = dp[rindex][cindex] + col
        # print(dp)


        # print(dp)
        return max(dp[-1])





