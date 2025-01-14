class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        chars = [0] * 26

        numOdd = 0

        for i in s:
            chars[ord(i) - ord('a')] +=1
            val = chars[ord(i)-  ord('a')]
            if val% 2 == 1:
                numOdd += 1
            else:
                numOdd -= 1

    


        if  numOdd> k:
            return False
        return True







