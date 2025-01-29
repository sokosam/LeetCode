class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1,1,2,6,24,120,720,5040,40320,362880]
        m = [x for x in range(10)]

        def getDigit(k, n):
            if (n ) == 0 or k == 0: return ""
            val = (k - 1)//fact[n-1] + 1

            if val == 0: val = 1
            temp = val
            val = m[val]
            m.pop(temp)
        
            return str(val) + getDigit(k%fact[n-1], n -1)
        res = getDigit(k,n)

        for i in range(len(m) - 1, 0, -1):
            if m[i] <= n and str(m[i]) not in res and len(res) != n:
                res += str(m[i])
        return res