class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        queue = deque()
        if grid[0][0] == 0: queue.append((0,0,1))
        dirs = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (1,1), (1,-1), (-1,1)]
        while queue:
            x,y, amt = queue.popleft()
            if x == len(grid[0]) -1 and y == len(grid) - 1:
                return amt
            for dx, dy in dirs:
                if dx +x >= 0 and dx +x < len(grid[0]) and dy + y >= 0 and dy + y < len(grid) and grid[dy + y][dx + x] == 0:
                    queue.append((dx + x, dy + y, amt + 1))
                    grid[y + dy][x + dx] = 1
            

        return -1
