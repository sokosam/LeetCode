class Solution:
    def punishmentNumber(self, n: int) -> int:
        

        """

        1296
        
        129 + 6 or   129 + x6 




        """
        def check(n, val, curr, res, step):
            
            # if curr > n or res >n  or curr + res > n:
            #     return False
            if val + curr + res == n:
                return True
            if val == 0:
                return False
            
            new = val% 10
            newVal = val//10
            if check(n, newVal, 0, res + curr + new*(10**(step)), 0):
                return True
            if check(n, newVal, curr + new*(10**(step)), res, step + 1):
                return True
            return False

            # if check(n, val//10, curr + new* 10**(step), res, step + 1):
            #     return True
            # if check(n, val//10, new, res + curr, 1)


        ans = 0
        for i in range(1,n + 1):
            sq = i*i
            if (i%9==0 or i%9==1) and check(i, sq, 0, 0 ,0):
                # print(i)
                ans += sq
        
        return ans