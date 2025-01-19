class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
        ans = [1]* n
        MOD = 10**9 + 7

        for i in range(k):
            for j in range(len(ans)):
                if j == 0:
                    ans[j] = 1
                else:
                    ans[j] = ans[j]  + ans[j -1] 
        return ans[-1]% MOD
