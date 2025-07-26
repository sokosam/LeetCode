class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word2) == 0:
            return len(word1)
        if len(word1) == 0:
            return len(word2)
        dp = [[float('inf') for _ in range(len(word1) + 1)]for k in range(len(word2) + 1)]
        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if row == len(word2) :
                    dp[row][col] = len(word1) - col
                if col == len(word1) :
                    dp[row][col] = len(word2) - row

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

        
        x = helper(0,0)
        return x