class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def outside(row,col, board):
            return not( 0<= row < len(board) and 0 <= col < len(board[0]))

        def canTouchEdge(row,col, board):
            seen = set()
            q = deque()
            dirs = [(1,0),(0,1), (-1,0), (0,-1)]
            x,y = row,col
            q.append((row,col))
            while q:
                curr = q.popleft()
                seen.add(curr)
                if outside(x,y,board):
                    return True
                x,y = curr[0], curr[1]
                for dx,dy in dirs:
                    new = (x+dx, y+dy)
                    if outside(x+dx,y+dy,board):
                        return True
                    if  new not in seen and board[x + dx][y +dy] == board[x][y]:
                        q.append(new)
                        seen.add(new)

            return False

        dirs = [(1,0),(0,1), (-1,0), (0,-1)]

        canTouch = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                for dx,dy in dirs:
                    newX,newY = row+dx, col +dy
                    if not outside(row+dx,col+dy,board):
                        if canTouch[newX][newY] == 1 and board[newX][newY] == board[row][col]:
                            canTouch[row][col] = 1
                        if canTouch[newX][newY] == 2 and board[newX][newY] == board[row][col]:
                            canTouch[row][col] = 2
                    
                if canTouch[row][col] == 0:
                    if canTouchEdge(row,col,board):
                        canTouch[row][col] = 1
                    else:
                        canTouch[row][col] = 2
        for row in range(len(board)):
            for col in range(len(board[0])):
                if canTouch[row][col] == 2:
                    val =board[row][col]
                    if val == "O":
                        board[row][col] = "X"




                
