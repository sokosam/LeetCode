class Solution:
    def grayCode(self, n: int) -> List[int]:
        seen = set()
        ans = [-1]* 2**n
        base = [0]* n

                

        def binToDeci(num):
            ans = 0
            power = len(num) -1
            for i in num:
                ans += 2 ** power if i == 1 else 0
                power -= 1
            return ans

        def bt(base,ans,i):
            val = binToDeci(base)
            if val in seen:
                return False
            else:
                seen.add(val)
                ans[i] = val
            if i >= len(ans) - 1:
                return True
            
            for j in range(len(base)):
                base[j] = 1 ^ base[j]
                check = bt( base, ans, i+ 1)
                if check: return True
                base[j] = 1 ^ base[j]
            seen.remove(val)
            ans[i] = -1
            return False
        bt(base,ans,0)
        return ans



