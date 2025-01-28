class Solution:
    def validPalindrome(self, s: str) -> bool:
    


        def skip(s, i):
            l = 0
            r = len(s) -1

            while l <= r:
                if l == i:
                    l +=1
                    continue
                if r == i:
                    r -= 1
                    continue
                else:
                    if s[l] != s[r]: return False
                    l += 1
                    r -= 1
            return True
        
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return skip(s, l) or skip(s, r)
            else:
                l += 1
                r -= 1
        return True
        