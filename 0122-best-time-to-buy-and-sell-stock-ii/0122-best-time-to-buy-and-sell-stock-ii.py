class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total = 0 
        curr = float('inf')

        for i in prices:
            if i < curr:
                curr = i
            else:
                total += i - curr
                curr = i
        return total