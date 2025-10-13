class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        def canMove(row,col):
            nonlocal board
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        dirs = [(-1,0), (0,-1)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if (not canMove(row - 1, col) or board[row-1][col] == ".") and (not canMove(row, col - 1) or board[row][col -1] == ".") and board[row][col] == "X":
                    count +=1
        return count