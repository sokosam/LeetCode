class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")

        ans = 0
        for word in words:
            for i in word:
                if i in brokenLetters:
                    ans +=1 
                    break
        return len(words) - ans