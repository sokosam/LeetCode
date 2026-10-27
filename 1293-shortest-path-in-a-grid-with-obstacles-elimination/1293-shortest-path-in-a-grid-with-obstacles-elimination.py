class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        min_steps = defaultdict(lambda : -1)
        best = float('inf')
        q = deque()

        q.append((0,0,0,k))

        def isValid(row,col):
            nonlocal grid

            return row >=0 and col >=0 and row < len(grid) and col < len(grid[0])
        dirs = [(1,0),(0,1), (-1,0), (0,-1)]
        while q:
            row,col,steps, curr_k = q.popleft()
            if row == len(grid) -1 and col == len(grid[0]) -1:
                best = min(best, steps)
                break

            for dr,dc in dirs:
                new_row,new_col = row + dr, col + dc
                if isValid(new_row,new_col):
                    key = (new_row, new_col)
                    new_k_val = curr_k
                    if grid[new_row][new_col]:
                        new_k_val -=1
                    if new_k_val < 0:
                        continue

                    

                    if min_steps[key] < new_k_val:
                        min_steps[key] = new_k_val
                        q.append((new_row, new_col, steps + 1,new_k_val))

                

        if best == float('inf'):
            return -1
        return best

