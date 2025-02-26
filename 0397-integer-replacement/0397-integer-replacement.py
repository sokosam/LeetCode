class Solution:
    def integerReplacement(self, n: int) -> int:
        
        
        dp = {1: 0}
        def check(n):
            if n in dp:
                return dp[n]
            if n%2 == 0:
                val = check(n//2) + 1
                dp[n] = val
                return val
            else:
                val =  min(check(n +1) +1, check(n-1)+ 1)
                dp[n] = val
                return val
        
        return check(n)
