class Solution:
    def minimumLength(self, s: str) -> int:
        m = {}
        ans = 0
        for i in s:
            if i not in m:
                m[i] = 1
                ans += 1
            elif m[i] == 2:
                m[i] = 1
                ans -= 1
            else:
                m[i] += 1
                ans += 1
        
            

        return ans

# the idea is that when a character has odd count they contribute only 1
# when it is even, they contribute two

