class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        """
        bbaab

        """
        ans = 0
        cnta =0 
        cntb = 0

        for i in s:
            if x >= y and i == "b":
                if cnta > 0:
                    cnta -=1
                    ans += x
                else:
                    cntb += 1
            elif x >= y and i =="a":
                cnta += 1
            elif y > x and i == "a":
                if cntb > 0:
                    cntb -=1
                    ans += y
                else:
                    cnta += 1
            elif y > x and i=='b':
                cntb+=1
            else:
                ans += min(x,y)*(min(cnta,cntb))
                cnta=0
                cntb=0
        ans += min(x,y)*(min(cnta,cntb))
        return ans 
 
