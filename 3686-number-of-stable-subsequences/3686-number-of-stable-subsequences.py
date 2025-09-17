class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        """
            
            [2,3,4,2,3,5,2,1]

            222 [2221]
            242 242 
            422


        """
        oneOdd = 0
        oneEven = 0
        twoOdd = 0
        twoEven = 0
        for i in nums:
            if i %2 == 0:
                twoEven += oneEven
                oneEven += oneOdd + twoOdd + 1
            else:
                twoOdd +=oneOdd
                oneOdd += oneEven + twoEven + 1
        return( oneOdd + oneEven + twoOdd + twoEven)% (10**9 + 7)