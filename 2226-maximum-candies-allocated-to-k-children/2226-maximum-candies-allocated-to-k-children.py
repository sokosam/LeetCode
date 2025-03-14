class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = float('-inf')

        total = 0
        for i in candies:
            low = max(low, i)
            total += i
        if total < k:
            return 0
        
        def isPossible(candies, k, amt):
            total = 0
            for i in candies:
                total += i//amt
            return total >= k
        
        l = 1
        r = low
        best = 0
        while l <= r:
            m = l + (r-l)//2
            if isPossible(candies, k, m) :
                best = max(best, m)
                l = m + 1
            else:
                r = m -1
        return best
            

        
        