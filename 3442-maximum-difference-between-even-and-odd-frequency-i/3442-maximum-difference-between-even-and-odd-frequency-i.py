class Solution:
    def maxDifference(self, s: str) -> int:
        vals = Counter(s)

        even = 101
        odd = 0
        for k in vals:
            if vals[k] % 2 ==0:
                even = min(even,vals[k])
            else:
                odd = max(odd, vals[k])
            # if vals[k] % 2 == 0:
            #     even = vals[k]
        
        return odd - even
