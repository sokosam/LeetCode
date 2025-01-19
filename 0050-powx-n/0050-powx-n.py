class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        inverse = 1
        if n < 0:
            n = -n
            inverse = -inverse
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *=x
            n//=2
        
        return ans**inverse
            