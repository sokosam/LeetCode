class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) % 2 ==0:
            x = Counter(s)
            for i in x:
                if x[i] % 2 ==1:
                    return False
            return True
        else:
            ones = 0
            x = Counter(s)
            for i in x:
                if x[i] % 2 ==1:
                    ones+=1
            return ones <= 1