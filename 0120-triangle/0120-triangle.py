class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        ans = float('inf')
        for i in range(len(triangle)):

            if i == 0:
                curr_min = triangle[i][0]
                ans = curr_min
                continue
            curr_min = float('inf')
            for j in range(len(triangle[i])):
                left = float('inf')
                right = float('inf')
                if j -1 >= 0:
                    left = triangle[i - 1][j -1]
                if j  < len(triangle[i-1]):
                    right = triangle[i-1][j]
                
                triangle[i][j] = min(triangle[i][j] + left, triangle[i][j] + right)
                curr_min = min(curr_min, triangle[i][j])
            ans = curr_min
        return ans