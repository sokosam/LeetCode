class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """

        1- 10

        

        x1 - x2

        (x2 - x1)//2 + ((x2-x1)//2 


        """

        dp = {}

        def getCost(start, end):
            if start >= end:
                return 0

            if (start,end) in dp:
                return dp[(start,end)]

            for i in range(start, end + 1):
                left = getCost(start, i - 1)
                right = getCost(i + 1, end)
                if (start,end) not in dp:
                    dp[(start,end)] = max(left + i, right + i)
                else:
                    dp[(start,end)] = min(dp[(start,end)],max(left + i, right + i)  )
            return dp[(start,end)]
        if n == 1:
            return 0
        return getCost(1,n)