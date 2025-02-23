class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        if numRows == 1: return s
        rows = [""]* numRows
        add = 1
        curr = 0


        for i in range(len(s)):

            rows[curr] += s[i]
            curr += add
            if curr == numRows - 1:
                add = -1
            if curr == 0:
                add = 1


        
        ans = ""
        for i in rows:
            ans += i
        return ans