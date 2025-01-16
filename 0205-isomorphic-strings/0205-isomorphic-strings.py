class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def check(s,t):
            mapp = {}
            seen = set()

            for i in range(len(s)):
                val = s[i]
                mapped = False
                if s[i] in mapp:
                    val = mapp[s[i]] 
                    mapped= True
                if val != t[i]:
                    if mapped: return False
                    if t[i] in seen: return False
                    mapp[val] = t[i]
                seen.add(t[i])
            return True
        return check(s,t) and check(t,s)


        return True


            