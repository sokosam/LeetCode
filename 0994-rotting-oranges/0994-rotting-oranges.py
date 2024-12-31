class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        again = True
        time = 0
        while again:
            again = False
            time += 1
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 2:
                        queue.append((row,col))
                        grid[row][col] = 0
                        
        
            while queue:
                curr = queue.popleft()

                row = curr[0]
                col = curr[1]

                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    again = True
                if row - 1 >= 0 and grid[row -1][col] == 1:
                    grid[row - 1][col] = 2
                    again = True

                if col - 1 >= 0 and grid[row][col -1] == 1:
                    grid[row][col -1] = 2
                    again = True

                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    grid[row][col + 1] =2
                    again = True
            if not again:
                time -=1

        for row in range(len(grid)):
            for col in range(len(grid[0])):      
                if grid[row][col] == 1: return -1
        return time
