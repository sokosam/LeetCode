class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0 
        grid = [[-k for k in i] for i in grid]
        m = len(grid[0])
        for row in grid:
            pos = bisect_left(row, 1)
            print(pos)
            ans +=m-pos

        return ans