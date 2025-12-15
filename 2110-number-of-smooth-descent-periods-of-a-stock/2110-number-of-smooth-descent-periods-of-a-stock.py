class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        l,r =0,1
        ans = 0


        while r < len(prices):
            if prices[r - 1] != prices[r] +1:
                summ = (r-l)*(r-l + 1)//2
                ans += summ
                l = r
            
            r +=1
        
        summ = (r-l)*(r-l + 1)//2
        ans += summ
        return ans
        
