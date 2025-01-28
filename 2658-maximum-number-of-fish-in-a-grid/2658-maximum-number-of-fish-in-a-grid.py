class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        # seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]


        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        # def dfs(row, col, val):

        #     # seen[row][col] = True
        #     gridVal = grid[row][col]
        #     val += gridVal
        #     grid[row][col] =0

        #     best_path = 0
        #     for dx ,dy in dirs:
        #         if self._isValid(row + dx, col + dy, grid) and grid[row +dx][col + dy] > 0:
        #             best_path =max(best_path, dfs(row +dx, col +dy, val))
            
        #     best_path = max(val, best_path)
        #     grid[row][col] = gridVal

        #     return best_path
        
        # ans = 0
        
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] > 0:
        #             ans = max(ans, dfs(row,col,  0))
        # return ans



        def bfs(row, col):
            val = 0


            q = deque()
            q.append((row,col))

            while q:
                row,col = q.popleft()
                val += grid[row][col]
                if grid[row][col] == 0:
                    continue

                grid[row][col] = 0
                for dx ,dy in dirs:
                    if self._isValid(row + dx, col + dy, grid) and grid[row +dx][col + dy] > 0:
                        q.append((row +dx, col + dy))
            return val
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans = max(ans, bfs(row, col))
        return ans
        
    def _isValid(self, row,col,grid):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])