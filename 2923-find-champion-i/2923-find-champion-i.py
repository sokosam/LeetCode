class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if row != col and grid[row][col] == 0:
                    break
                
                if col == len(grid[0]) -1:
                    return row
        
