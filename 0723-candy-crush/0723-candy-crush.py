class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def candiesToDestroy(board):
            def mark(element1, element2, element3):
                return element1 == element2 == element3

            for row in range(len(board)):
                for col in range(len(board[0])):
                    if (row == 0 and col == 0) or (row == 0 and col == len(board[0]) -1) or (row == len(board) -1 and col == 0) or (row == len(board) -1 and col == len(board[0]) -1):
                        continue
                    elif row == 0 or row == len(board) -1 :
                        if mark(abs(board[row][col]), abs(board[row][col -1]), abs(board[row][col + 1])):   
                            board[row][col] *= -1 if board[row][col] > 0 else 1
                            board[row][col -1] *= -1 if board[row][col -1] > 0 else 1
                            board[row][col + 1] *= -1 if board[row][col + 1] > 0 else 1
                    elif col == 0  or col == len(board[0]) -1:
                        if mark(abs(board[row][col]), abs(board[row + 1][col]), abs(board[row - 1][col])):
                            board[row][col] *= -1 if board[row][col] > 0 else 1
                            board[row + 1][col] *= -1 if board[row + 1][col] > 0 else 1
                            board[row - 1][col] *= -1 if board[row -1][col] > 0 else 1
                    else:
                        if mark(abs(board[row][col]), abs(board[row + 1][col]), abs(board[row - 1][col])):
                            board[row][col] *= -1 if board[row][col] > 0 else 1
                            board[row + 1][col] *= -1 if board[row + 1][col] > 0 else 1
                            board[row - 1][col] *= -1 if board[row -1][col] > 0 else 1
                        if mark(abs(board[row][col]), abs(board[row][col -1]), abs(board[row][col + 1])):
                            board[row][col] *= -1 if board[row][col] > 0 else 1
                            board[row][col -1] *= -1 if board[row][col -1] > 0 else 1
                            board[row][col + 1] *= -1 if board[row][col + 1] > 0 else 1
        
        def replaceCandies(board):
            replaced = 0
            for col in range(len(board[0])):
                q = deque()
                for row in range(len(board) -1, -1 ,-1):
                    if board[row][col] < 0:
                        q.append([row,col])
                        board[row][col] = 0
                    else:
                        if len(q) > 0:
                            newPos = q.popleft()
                            board[newPos[0]][newPos[1]] = board[row][col]
                            replaced +=1
                            board[row][col] = 0
                            q.append([row,col])
            return replaced

        x = 0
        candiesToDestroy(board)
        x = replaceCandies(board)
        while x > 0:
            candiesToDestroy(board)
            x = replaceCandies(board)
        return board



                                    