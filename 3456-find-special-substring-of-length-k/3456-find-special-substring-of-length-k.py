class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        
        chars = [0]*26


        l = 0
        r = k 

        for i in range(k):
            index = ord(s[i]) - ord('a')

            chars[index] += 1
            if chars[index] == k:
                if i + 1 >= len(s): return True
                if i + 1 < len(s) and s[i + 1] != s[i]:
                    return True
        
        
        while r < len(s):
            rindex = ord(s[r]) - ord('a')
            lindex = ord(s[l]) - ord('a')
            chars[rindex] += 1
            chars[lindex] -= 1
            print(chars)

            if chars[rindex] == k:
                possible = True
                print(s[l + 1:r])
                
                possible = possible and s[l] != s[r]
                if r + 1 < len(s):
                    possible = possible and s[r + 1] != s[r]

                if possible:
                    return True
            r += 1
            l += 1
        return False
