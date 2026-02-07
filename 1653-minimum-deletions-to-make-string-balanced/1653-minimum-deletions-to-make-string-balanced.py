class Solution:
    def minimumDeletions(self, s: str) -> int:
        

        """


        b [2, 1, 1, 0]

        [2, 2 ,2, 1, 1,1,0,0]
        [2,2]

        a [0, 0, 1 ,3]
        [0,0, 0, 1,1,1,3,3]
        [0,0,]



        """

        
        seenb= 0
        totalAs = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'a':
                totalAs +=1

        best = float('inf')
        for i in range(len(s)):
            if s[i] == 'a':
                totalAs -= 1
            best = min(best, totalAs + seenb)
            if s[i] == 'b':
                seenb +=1
        return best