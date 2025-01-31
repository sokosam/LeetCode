class Solution:
    def partitionString(self, s: str) -> int:
        count = [0] * 26
        ans = 0
        for char in s:
            if count[ord(char) - ord('a')] > 0:
                ans +=1
                count = [0] *26
            count[ord(char) - ord('a')] +=1
        if sum(count) > 0:
            ans +=1
        return ans
