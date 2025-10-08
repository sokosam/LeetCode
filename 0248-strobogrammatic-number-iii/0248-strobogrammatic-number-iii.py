class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def findStrobogrammatic( n: int) -> List[str]:
            available = [1,0,8,6]
            ans = []
            curr = [-1]*n
            def recurse(l,r):
                nonlocal curr
                if l > r:
                    ans.append("".join(curr.copy()))
                    return
                
                else:
                    for num in available:
                        if num != 6:
                            if num == 0 and l == 0 and l != r:
                                continue
                            curr[l] = str(num)
                            curr[r] = str(num)
                            recurse(l + 1, r -1)
                        else:
                            if l == r:
                                continue
                            curr[l] = "6"
                            curr[r] = "9"
                            recurse(l + 1, r - 1)
                            curr[l] = "9"
                            curr[r] = "6"
                            recurse(l + 1, r- 1)
            recurse(0, n- 1)
            return ans
        ans = 0
        left = int(low)
        right = int(high)
        for i in range(len(low), len(high)  +1):
            strobs = findStrobogrammatic(i)
            for strob in strobs:
                if left <= int(strob) <= right:
                    ans +=1
        return ans