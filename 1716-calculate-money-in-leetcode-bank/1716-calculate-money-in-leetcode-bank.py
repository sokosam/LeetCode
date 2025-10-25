class Solution:
    def totalMoney(self, n: int) -> int:
        cycles = n//7
        days = n%7
        return 7*(cycles*(cycles -1)//2) + 28*cycles + cycles*days + days*(days +1)//2

        """
        1 2 3 4 5 6 7 = 0 + (1 2 3 4 5 6 7)
        2 3 4 5 6 7 8 = 7 + (1 2 3 4 5 6 7)
        3 4 5 6 7 8 9 = 14 + (1 2 3 4 5 6 7)
        4 5 6  =        cycles*days + days*(days + 1)//2


        """