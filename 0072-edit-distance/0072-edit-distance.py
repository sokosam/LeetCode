class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        m, n = len(word2), len(word1)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m] = [n - i for i in range(n + 1)]
        for j in range(m + 1):
            dp[j][n] = m - j


        def helper(i,j):
            if dp[j][i] != float('inf'):
                return dp[j][i]
            if i >= len(word1):
                return float('inf')
            delete = helper(i + 1,j)
            continued = float('inf') if word1[i] != word2[j] else helper(i +1, j + 1)
            replace = helper(i + 1, j + 1)
            insert = helper(i, j + 1)
            best = min(delete+1,continued,replace+1,insert+1)
            dp[j][i] = best
            return best

        
        return helper(0,0)
