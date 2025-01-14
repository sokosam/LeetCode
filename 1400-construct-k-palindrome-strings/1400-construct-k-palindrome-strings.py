class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        chars = [0] * 26

        for i in  s:
            chars[ord(i) - ord('a')] +=1

    
        numOdd = 0
        numEven = 0
        single = 0

        for i in range(26):
            if chars[i] == 1:
                single += 1
            elif chars[i] % 2 == 0:
                numEven += 1
            else:
                numOdd += 1




        if single + numOdd> k:
            return False

        return True







