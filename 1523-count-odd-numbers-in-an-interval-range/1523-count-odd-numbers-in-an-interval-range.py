class Solution:
    def countOdds(self, low: int, high: int) -> int:
        

        # 7 - 2 = 5  
        #  5 

        # 8 - 2 = 6


        if (high - low +1  )% 2 == 1:
            return (high-low + 1)//2 + (low % 2)
        else:
            return (high-low + 1)//2