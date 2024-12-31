class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]  
        pacific = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]  
        print(atlantic)
        print(pacific)
        def check(ocean, row, col):
            if ocean[row][col]:
                return
            
            ocean[row][col] = True

            if row + 1 < len(heights) and heights[row + 1][col] >= heights[row][col]:
                check(ocean, row + 1, col)
            if row - 1 >= 0 and heights[row -1][col] >= heights[row][col]:
                check(ocean, row - 1, col)
            if col + 1 < len(heights[0]) and heights[row][col + 1] >= heights[row][col]:
                check(ocean, row, col +1)
            if col - 1 >= 0 and heights[row][col -1] >= heights[row][col]:
                check(ocean, row, col -1)
            
        
        for i in range(len(heights[0])):
            check(pacific,0, i)
            check(atlantic, len(heights) - 1, i)

        for i in range(len(heights)):
            check(pacific, i, 0)
            check(atlantic, i, len(heights[0]) - 1)

        ans = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if atlantic[row][col] and pacific[row][col]:
                    ans.append([row,col])
        return ans