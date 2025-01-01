class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        right = 0
        for i in s:
            if i == '1':
                right +=1
        
        left = 0
        for i in s:
            if i == '0':
                left +=1
            else:
                right -= 1
            
            ans = max(left + right, ans)
        return ans
            