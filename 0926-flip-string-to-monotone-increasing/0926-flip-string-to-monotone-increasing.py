class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """

        00011010000
        islands of 1s
        
        100111111100101110
        locally it makes to flip the 1 since we can save 2 flips for 0 if we do so
        10010011110000000000101

        the idea is we keep a 1, all future 0s must be 1s aswell, thus we can make a decsion
        at the next 1,
        up to the previous iteration, is it more worthwhile to swap the 1 to a zero or swap all zeroes to a 1 and forcefully make all zeroes in the future aswell into 1s?

        We can calulate this by:
        cost1 = #total zeroes - #seen zeroes
        cost2 = #number of 1s counted before

        we can accept the min and update for our future iteration

        100111111100101110
           ^
        c = 1 since # of 1s = 1 and totalzeroes = 6

        111111100101110 total cost = 1
                 ^
                 c = 4 since #1s = 7 and total zeroes = 4
                 since we picked this other option, we should end searching as everything must default to 1
                
        total cost = 5

        "111011100100100"


        "1110001110
        """
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0
        for c in s:
            if c == '0':
                ans = min(num, ans + 1)
            else:
                num += 1
        return ans