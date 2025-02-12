class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        matrix = [[int(x) for x in row] for row in matrix]

        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                
                if row == 0 or col == 0:
                    ans = max(ans, matrix[row][col])
                    continue
                
                if matrix[row][col] == 0:
                    continue
                maxSquare = min(matrix[row -1][col -1], matrix[row-1][col], matrix[row][col -1])

                if maxSquare + 1 <= 1:
                    ans = max(ans, matrix[row][col])
                else:
                    matrix[row][col] = maxSquare + 1
                    ans = max(ans,matrix[row][col])
        return ans*ans               
