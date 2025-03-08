class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l = 0
        r = k 
        chars = [0]*26
        ans = 0
        if k > len(s):
            return 0

        for i in range(k):
            index = ord(s[i]) - ord('a')
            chars[index] += 1
            if chars[index] > 1:
                ans = -1
        ans += 1

        while r < len(s):
            indexLeft = ord(s[l]) - ord('a')
            indexRight = ord(s[r]) - ord('a')
            chars[indexLeft] -=1
            chars[indexRight] +=1

            add = 1
            # print(chars)
            for i in chars:
                if i > 1:
                    add = 0
            ans += add
            l+=1
            r+=1
        return ans
                    