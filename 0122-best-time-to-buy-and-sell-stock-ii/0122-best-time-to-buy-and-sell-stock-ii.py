class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        7 1 5 3 6 4
        7 1 1 1 1 1
        7 6 6 6 6 4


        """

        total = 0 
        curr = float('inf')

        for i in prices:
            if i < curr:
                curr = i
            else:
                total += i - curr
                curr = i
        return total