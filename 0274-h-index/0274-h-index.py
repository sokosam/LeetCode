class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l = 0
        r = min(len(citations), max(citations))

        def verify(citations, h):
            count = 0 
            for i in citations:
                if i >= h: count +=1
            return count >= h 
        

        ans = 0
        while l <= r:
            m = l + (r-l)//2

            check = verify(citations,m)
            if check:
                l = m + 1
                ans = max(ans, m)
            else:
                r = m -1
        return ans
            