class Solution:
    def hIndex(self, citations: List[int]) -> int:
        

            """ 


            h_indexAtPaperi =  min(len(subarryFromiToEnd),hVal)

            """


            ans = 0

            l = 0
            r = len(citations) - 1
            total = len(citations) 
            while l <=r:

                m = l + (r-l)//2

                if citations[m] == total - m:
                    return total - m
                elif citations[m] > total - m:
                    ans = max(ans, total - m)
                    r = m -1
                else:
                    if citations[m] >= m + 1:
                        ans= max(ans, 1)
                    l = m + 1
            return ans