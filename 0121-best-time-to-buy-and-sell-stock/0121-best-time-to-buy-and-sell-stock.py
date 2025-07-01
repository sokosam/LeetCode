class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        minPrice = float("inf")
        for i in prices:
            minPrice = min(minPrice, i)
            ans = max(i - minPrice, ans)
        return ans