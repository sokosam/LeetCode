class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        



        dp = {}
        def getPower(x):
            if x == 1:
                return 0
            if x in dp:
                return dp[x]
            ans = 1 + getPower(x//2) if x % 2 ==0 else 1 + getPower(3*x + 1)
            dp[x] = ans
            return ans

        ans =[(x,getPower(x)) for x in range(lo, hi + 1)]
        ans.sort(key = lambda x : x[1])
        return ans[k- 1][0]