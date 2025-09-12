class Solution:
    def customSortString(self, order: str, s: str) -> str:
        

        m = Counter(s)
        ans = ""

        for i in order:
            if i in m:
                ans += i*m[i]
                del m[i]
        
        for i in m:
            ans += m[i]*i
        return ans