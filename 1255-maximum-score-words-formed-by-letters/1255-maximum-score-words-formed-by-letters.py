class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        l = [0]*26
        ans = 0

        for letter in letters:
            l[ord(letter) - ord('a')] += 1


        def bt(l, i, curr):
            if i >= len(words):
                return curr
            
            noAdd = bt(l, i + 1, curr)

            pts=  0
            isPossible = True
            for letter in words[i]:
                l[ord(letter) - ord('a')] -= 1
                pts += score[ord(letter) - ord('a')]
                if l[ord(letter) - ord('a')] < 0:
                    isPossible = False
            
            add = 0

            if isPossible:
                add = bt(l, i + 1, curr + pts)
            
            for letter in words[i]:
                l[ord(letter) - ord('a')] += 1
            
            return max(noAdd, add)

        return bt(l, 0, 0)            
