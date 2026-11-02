class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    q.append((row,col, 0))


        safety_arr = [[float('inf')]*(len(grid[0])) for _ in range(len(grid))]

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]   

        def isValid(row,col):
            nonlocal grid,dirs

            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
        while q:
            row,col,safety = q.popleft()
            safety_arr[row][col] = min(safety_arr[row][col], safety)

            for dr,dc in dirs:
                new_row, new_col = row + dr, col +dc
                if isValid(new_row, new_col) and safety_arr[new_row][new_col] > safety + 1:
                    safety_arr[new_row][new_col] = safety + 1
                    q.append((new_row, new_col, safety + 1))

        def isPossible(k):

            nonlocal grid,dirs, safety_arr

            seen = set()
            q = deque()
            seen.add((0,0))
            q.append((0,0))
            if safety_arr[0][0] < k:
                return False

            while q:
                row,col = q.popleft()
                if row == len(grid)-1 and col == len(grid[0])-1:
                    return True

                for dr,dc in dirs:
                    nr,nc = row+dr,col+dc
                    if isValid(nr,nc) and (nr,nc) not in seen and safety_arr[nr][nc] >= k:
                        q.append((nr,nc))
                        seen.add((nr,nc))
            return False


        l = 0
        r = 0

        for row in safety_arr:
            for col in row:
                l = min(l,col)
                r = max(r, col)

        # best = r
        while l<=r:
            m = l + (r-l)//2

            if isPossible(m):
                l = m + 1
                # best = min(best, m)
            else:
                r= m - 1
        return r