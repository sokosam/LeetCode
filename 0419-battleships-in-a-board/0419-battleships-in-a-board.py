class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 1

        q = deque()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def canMove(row,col):
            nonlocal board
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        for row in range(len(board)):
            for col in range(len(board[0])):
                found = False
                if board[row][col] == "X":
                    q.append((row,col))
                    found = True

                while q:
                    r,c = q.popleft()
                    board[r][c] = count

                    for dr,dc in dirs:
                        if canMove(r+dr,c+dc) and board[r+dr][c+dc] == "X":
                            q.append((r +dr, c+dc))
                            board[r+dr][c+dc] = count
                if found:
                    count +=1
        return count - 1

