class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
    

        prefix = 0

        numOdds =0 
        numEvens = 0
        ans = 0

        for i in arr:
            prefix += i

            if prefix % 2 ==0:
                ans += numOdds
                numEvens +=1
            else:
                ans+= numEvens + 1
                numOdds += 1
        return ans %(10**9 + 7)
