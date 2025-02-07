class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        m = {'N': 0, 'E': 0, "S" : 0, 'W' :0}

        ans = 0
        for i in s:
            m[i] +=1
        

            ydir = max(m["N"], m['S'])
            badY = min(m["N"], m['S'])

            xdir = max(m["E"], m["W"])
            badX = min(m["E"], m["W"])

            totalBad = badY + badX
            makePos = min(k, totalBad)
            totalBad -= makePos
            ans = max(ydir + xdir + makePos - totalBad,ans)
        return ans