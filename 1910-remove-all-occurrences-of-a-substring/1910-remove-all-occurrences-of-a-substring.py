class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        l = 0
        r = len(part) - 1


        while r < len(s):
            curr = s[l:r+1]
            if curr == part:
                return self.removeOccurrences(s[0:l] + s[r+1:], part)
            l += 1
            r += 1
        return s