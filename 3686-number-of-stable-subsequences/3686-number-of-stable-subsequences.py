class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        """
            
            [2,3,4,2,3,5,2,1]

            222 [2221]
            242 242 
            422


        """
        MOD =  (10**9 + 7)
        oneOdd = 0
        oneEven = 0
        twoOdd = 0
        twoEven = 0
        for i in nums:
            if i %2 == 0:
                twoEven += oneEven % MOD
                oneEven += (oneOdd + twoOdd + 1)% MOD
            else:
                twoOdd +=(oneOdd)% MOD
                oneOdd += (oneEven + twoEven + 1)% MOD

        return( oneOdd + oneEven + twoOdd + twoEven) % MOD