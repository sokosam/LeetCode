class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        


        ans = 0
        water = numBottles
        empty = 0
        while (empty + water)//numExchange > 0:
            ans += water
            empty = empty + water
            water = empty//numExchange
            empty = empty % numExchange


        return ans + water