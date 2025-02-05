class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def LCS(text1, text2, i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            case1 = LCS(text1, text2, i + 1, j)

            case2 = 0
            loc = -1
            for index in range(j, len(text2)):
                if text1[i] == text2[index]:
                    loc = index
                    break

            if loc >= 0:
                case2 = LCS(text1, text2, i + 1, loc + 1) + 1

            dp[i][j] =max(case2, case1)
            return dp[i][j]
        return LCS(text1,text2,0,0)