class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen = {}
        ans = []
        l = 0
        r = 10
        while r <= len(s):
            if s[l:r] in seen and not seen[s[l:r]]:
                seen[s[l:r]] = True
                ans.append(s[l:r])
            elif s[l:r] not in seen:
                seen[s[l:r]] = False
            l+=1
            r+=1
        return ans
