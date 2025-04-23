class Solution:
    def countLargestGroup(self, n: int) -> int:
        m = {}
        best = 0
        bestSize = 0

        for i in range(1,n + 1):
            x = str(i)
            val = 0

            for j in x:
                val += int(j)
            
            if val in m:
                m[val] +=1
            else:
                m[val] = 1
            
            if m[val] > best:
                best = m[val]
                bestSize = 1
            elif m[val] == best:
                bestSize +=1
        return bestSize
        
    
