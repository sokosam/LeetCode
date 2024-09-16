# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/valid-sudoku/submissions/1391599111/
# Time Complexity: O(1) ~ Technically because the board is always 9x9
# Space Complexity: O(1) ~ Technically because the board is always 9x9

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def is3x3Valid(arr : list[list[str]])->bool:
            print(arr)
            seen = set()
            for i in arr:
                for k in i:
                    if k != ".":
                        if k in seen:
                            return False
                        else: seen.add(k)
            return True
        
        first_3_rows = board[0:3]
        second_3_rows = board[3:6]
        third_3_rows = board[6:]

        def get3x3(inp : list[list[str]])-> list[list[str]]:
            return [[inp[0][0:3], inp[1][0:3], inp[2][0:3] ],[inp[0][3:6], inp[1][3:6], inp[2][3:6] ], [inp[0][6:], inp[1][6:], inp[2][6:] ] ]

        valid = True
        for i in get3x3(first_3_rows):
            valid= is3x3Valid(i)
            if not valid:
                return False
        for i in get3x3(second_3_rows):
            valid= is3x3Valid(i)
            if not valid:
                return False
        for i in get3x3(third_3_rows):
            valid= is3x3Valid(i)
            if not valid:
                return False

        def checkRowValid(row: list)->bool:
            seen = set()
            for i in row:
                if i !=".":
                    if i in seen:
                        return False
                    else:
                        seen.add(i) 
            return True
        
        def checkColumnValid(arr: list[list[str]])->bool:
            for i in range(9):
                seen=set()
                for k in range(9):
                    if arr[k][i] != ".":
                        if arr[k][i] in seen:
                            return False
                        else:
                            seen.add(arr[k][i])
            return True
                        

        valid_rows = True

        for i in board:
            valid_rows = checkRowValid(i)
            if not valid_rows:
                return False

        return valid and checkColumnValid(board)


# Completed on: 7/14/2023
# Submission: https://leetcode.com/problems/valid-sudoku/submissions/994435365/
# Time Complexity: O(1) ~ Technically because the board is always 9x9
# Space Complexity: O(1) ~ Technically because the board is always 9x9

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        l = []
        for row in board:
            l = []
            for element in row:
                if element in l and element != ".":
                    return False
                else:
                    l.append(element)
        for col in range(len(board)):
            l = []
            for element in range(9):
                if board[element][col] in l and board[element][col] != ".":
                    return False
                else:
                    l.append(board[element][col])

        times = 1
        for sr in range(3):
            for sc in range(3):
                l = []
                for r in range(3):
                    if board[ sr*3][r + sc * 3] in l and board[ sr*3][r + sc * 3] != ".":
                        return False
                    else:
                        l.append(board[sr*3][r + sc * 3])
                for r in range(3):
                    if board[1 + sr*3][r + sc * 3] in l and board[1 +  sr*3][r + sc * 3] != ".":
                        return False
                    else:
                        l.append(board[1 + sr*3][r + sc * 3])
                for r in range(3):
                    if board[2 + sr*3][r + sc * 3] in l and board[2 + sr*3][r + sc * 3] != ".":
                        return False
                    else:
                        l.append(board[2 + sr*3][r + sc * 3])
        return True
        
        
