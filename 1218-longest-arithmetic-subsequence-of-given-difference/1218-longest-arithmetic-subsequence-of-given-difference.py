class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = defaultdict(int)

        for i in arr:
            x1 = i - difference
            dp[i] = max(dp[i], 1 + dp[x1])
        return max(dp.values())
