class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        dp = [[2 for _ in range(len(s))] for _ in range(len(wordDict))]

        def helper(i):
            if i == len(s):
                return True
            ans = False
            for idx,j in enumerate(wordDict):
                if dp[idx][i] != 2:
                    ans = ans or dp[idx][i]
                    continue
                size =len(j)
                if i + size <= len(s):
                    if s[i:i + size] == j:
                        ans = ans or helper(i + size)
            dp[idx][i] = ans
            return ans
        x =helper(0)
        return bool(x)