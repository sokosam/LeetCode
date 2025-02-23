class Solution:
    def numTrees(self, n: int) -> int:
        """



        1 2 3 4 5

           3
        12   45
      2       4     5
    1           5 4


        """

        dp = [[-1 for _ in range(20)] for _ in range(20)]
        def helper(l, r):
            if r - l <= 0:
                return 1

            
            ans = 0
            for i in range(l, r + 1):
                if i - 1 - l <= 0:
                    left = 1
                elif dp[l][i -1] != -1:
                    left = dp[l][i-1]
                else:
                    left = helper(l, i -1)
                    dp[l][i-1] = left

                if r - i - 1 <= 0:
                    right = 1
                elif dp[i + 1][r] != -1:
                    right = dp[i+1][r]
                else:
                    right = helper(i + 1, r)
                    dp[i +1][r] = right
                ans += left*right
            
            return ans
        return helper(1,n)

        """
        1 2 3

        1
         

        """