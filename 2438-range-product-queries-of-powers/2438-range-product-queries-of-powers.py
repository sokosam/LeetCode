class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        ans = []
        curr2 = 1
        m = []
        while n > 0:
            if n & 1:
                m.append(curr2)
            curr2*=2
            n>>=1

        prodSum = []
        curr = 0

        for i in m:
            if len(prodSum) == 0:
                curr = i
                prodSum.append(curr)
            else:
                curr*=i
                prodSum.append(curr)

        MOD = 10**9 + 7
        for q in queries:
            ans.append(prodSum[q[1]]//prodSum[q[0] - 1] % (MOD) if q[0] != 0 else prodSum[q[1]] % MOD)
        return ans
