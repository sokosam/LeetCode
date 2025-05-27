class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = {}

        for word in words:
            if word not in m:
                m[word] = [1, word[::-1]]
            else:
                m[word][0] +=1
        
        ans = 0
        mid = 0
        # print(m)
        for key in m:
            if m[key][1] not in m:
                continue
            if m[key][1] == key:
                ans += (m[key][0]//2)*4
                if m[key][0] % 2 == 1:
                    mid = 2
                continue
            ans += min(m[key][0], m[m[key][1]][0])*4
            m[m[key][1]][0] = 0
            m[key][0] = 0
        return ans + mid
