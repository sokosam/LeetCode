class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                left = triangle[i-1][j - 1] if j -1 >= 0 else float('inf')
                right = triangle[i-1][j] if j < len(triangle[i - 1]) else float('inf')
                triangle[i][j] = min(left, right) + triangle[i][j]
        return min(triangle[-1])