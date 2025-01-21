class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s= []
        ans = []
        for i in range(len(prices)-1, -1, -1):

            while len(s) >0 and prices[i] < s[-1]:
                s.pop()
            if len(s) == 0:
                s.append(prices[i])
                ans.append(prices[i])
            else:
                ans.append(prices[i] - s[-1])
                s.append(prices[i])
        ans.reverse()
        return ans
            