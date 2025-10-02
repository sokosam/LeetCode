class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        water = numBottles
        empty = 0
        ans = 0
        while empty + water >= numExchange:
            ans += water
            empty += water
            water = 0

            while empty >= numExchange:
                empty -=numExchange
                water +=1
                numExchange +=1
        return ans + water
