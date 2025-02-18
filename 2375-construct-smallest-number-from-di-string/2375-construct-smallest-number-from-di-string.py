class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        vals = [1]*10
        s = []
        ans = []

        def bt(i, s):
            if i >= len(pattern):
                a = ""                
                for i in s:
                    a += str(i)

                ans.append(a)
                return True
            
            for k in range(1, 10):

                if pattern[i] == 'I' and k <= s[-1]: continue
                if pattern[i] == 'D' and k >= s[-1]: continue
                if vals[k] == 0: continue
                s.append(k)
                vals[k] -= 1 
                if bt(i + 1, s): 
                    return True
                s.pop()
                vals[k] += 1
            
            return False
        
        for i in range(1, 10):
            vals[i] -= 1
            s.append(i)
            if bt(0, s):
                return ans[0]
            s.pop()
            vals[i] += 1

        return ""

