class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        c1 =Counter(start)
        c2 = Counter(result)
        if c1.get("R",0) != c2.get("R", 0) or c1.get("L",0) != c2.get("L", 0):
            return False

        R = []
        L = []
        for idx,i in enumerate(start):
            if i == "R":
                R.append(idx)
            elif i == "L":
                L.append(idx)

        
        rptr = 0
        lptr = 0
        for idx,i in enumerate(result):
            if i == "R":
                if rptr >= len(R):
                    return False
                if lptr < len(L) and L[lptr] < R[rptr]:
                    return False
                if lptr < len(L) and R[rptr] < L[lptr] <= idx:
                    return False
                if R[rptr] > idx:
                    return False
                rptr +=1

            elif i == "L":
                if lptr >= len(L):
                    return False
                if rptr < len(R) and R[rptr] < L[lptr]:
                    return False
                if L[lptr] < idx:
                    return False
                lptr +=1  
        return True


