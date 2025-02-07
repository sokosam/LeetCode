class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        words = {}
        freq = [0]*26

        unique = 0  
        l = 0
        r = 0

        ans = 0
        for i in range(minSize):
            index = ord(s[i]) - ord('a')

            freq[index] += 1
            if freq[index] == 1:
                unique += 1
            r += 1
        if unique <= maxLetters:
            words[s[l:r]] = 1
            ans = 1
        # print(words, freq)
        
        while r < len(s):
            index = ord(s[r]) - ord('a')
            freq[index] += 1
            unique += 1 if freq[index] == 1 else 0
            index2 = ord(s[l]) - ord('a')
            freq[index2] -= 1
            unique -= 1 if freq[index2] == 0 else 0
            if unique <= maxLetters:
                temp = s[l+ 1:r + 1]
                print(l + 1, r, temp)
                if temp in words:
                    words[temp] += 1 
                else:
                    words[temp] = 1
                ans = max(ans, words[temp])
            r += 1
            l += 1
        index = ord(s[l]) - ord('a')
        freq[index] -= 1
        unique -= 1 if freq[index] == 0 else 0

        return ans