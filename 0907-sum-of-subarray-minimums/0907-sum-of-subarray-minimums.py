class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10**9 +7
        ans = 0

        s = []
        add =0

        for i in range(len(arr)- 1,-1,-1):
            if len(s) == 0:
                s.append(i)
                ans += arr[i] % MOD
                add += (len(arr) - i)*arr[i]
                continue
            # prin
            while s and arr[s[-1]] >= arr[i]:
                x = s.pop()
                if len(s) > 0:
                    add -= (s[-1] - x )*arr[x]
                else:
                    add = 0 
            #     print(add)

            # print("pre: ", add)
            s.append(i)
            if len(s) > 1:
                add += (  s[-2] - s[-1])*arr[i]
            else:
                add += (len(arr) - s[0])*arr[i]
            ans += add % MOD
            # print("after" ,add)
            # print("ans ", ans)
            # print(s)
            # prev = len(arr)
            # for j in range(len(s)):
            #     ans += (arr[s[j]] *(prev - s[j])) % MOD
            #     prev = s[j]
        return ans % MOD
                




"""

[3,2,1,4]
3 2 1 1
2 1 1
1 1 
4

[3,2,3,1,4]
3 2 2 1 1
2 2 1 1
3 1 1
1 1
4
"""
