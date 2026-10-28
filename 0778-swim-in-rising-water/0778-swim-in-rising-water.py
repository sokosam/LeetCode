class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        r = max([max(i) for i in grid])
        l = grid[0][0]


        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def isValid(row,col):
            nonlocal grid

            return row >=0 and col >=0 and row < len(grid) and col < len(grid[0])

        def check(t):
            nonlocal grid, dirs
            q = deque()
            q.append((0,0))

            seen = set()
            seen.add((0,0))
            while q:
                row,col = q.popleft()
                if row == len(grid) -1 and col == len(grid[0]) - 1:
                    return True

                for dr,dc in dirs:
                    nrow,ncol = row + dr, col + dc
                    if isValid(nrow,ncol) and (nrow,ncol) not in seen and grid[nrow][ncol] <= t:
                        seen.add((nrow,ncol))
                        q.append((nrow,ncol))

            return False

        while l <=r:
            m = l + (r-l)//2

            if check(m):
                r = m -1
            else:
                l = m + 1
        return l