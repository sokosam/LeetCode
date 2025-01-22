class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        pq = deque()

        grid = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]


        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    pq.append((row,col))
                    grid[row][col] = 0
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        while len(pq) > 0:
            curr = pq.popleft()

            row = curr[0]
            col = curr[1]

            for dx, dy in directions:
                newRow = row+ dx
                newCol = col + dy

                if newRow >= 0 and newRow < len(mat) and newCol >=0 and newCol < len(mat[0]):
                    if grid[newRow][newCol] == -1:
                        grid[newRow][newCol] = grid[row][col] + 1
                        pq.append((newRow,newCol))
        
        return grid
