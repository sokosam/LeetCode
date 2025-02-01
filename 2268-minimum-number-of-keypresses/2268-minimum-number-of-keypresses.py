class Solution:
    def minimumKeypresses(self, s: str) -> int:
        vals = [9,9,8]

        chars = [0] * 26


        for i in s:
            chars[ord(i) - ord('a')] += 1
            # if chars[ord(i) - ord('a')] > 3: return -1
        
        pter = 0
        chars.sort(reverse = True)
        curr = 0
        ans = 0
        while curr < len(chars) and chars[curr] != 0:

            if vals[pter] == 0:
                pter += 1
            
            ans += chars[curr] * (pter + 1)
            curr +=1
            vals[pter] -= 1
        return ans