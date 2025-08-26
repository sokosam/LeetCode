class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        q = [0]*5
        m = {'c' : 0, 'r' : 1, 'o' : 2, 'a' : 3, 'k' : 4}

        best = 0
        ans = 0
        for i in croakOfFrogs:
            print(q)
            if m[i] == 0:
                q[m[i]] += 1
            elif q[m[i] - 1] == 0:
                return -1
            elif m[i] == 4:
                q[m[i] -1] -=1
                ans += 1
            else:
                q[m[i] - 1] -=1
                q[m[i] ]+=1
            best = max(sum(q),best)
        if sum(q) != 0:
            return -1
        return best

                
            