"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def all_same(start_row, start_col, end_row, end_col):
            nonlocal grid
            total = 0
            total_cells = (end_row - start_row +1)*(end_col - start_col +1)
            for row in range(start_row, end_row + 1):
                for col in range(start_col, end_col + 1):
                    total += grid[row][col]
            # print(total, start_row, start_col, end_row, end_col)
            return total == 0 or total == total_cells, total
        

        def create_tree(start_row, start_col, end_row, end_col):
            isSame, amount = all_same(start_row,start_col,end_row,end_col)
            if isSame:
                return Node(amount, True, None, None, None, None)
            

            """
            0 - 3      

            0 - 1

            2 - 3


            4 - 7
            5 

            (7 + 4) // 2 = 5
            """                 
            top_left = create_tree(start_row,start_col, (end_row + start_row)//2 , (end_col + start_col)//2)


            top_right = create_tree(start_row,  (end_col + start_col)//2 + 1, (end_row + start_row)//2, end_col)


            bottom_left = create_tree((end_row + start_row)//2 + 1, start_col, end_row,(end_col + start_col)//2 )


            bottom_right = create_tree((end_row + start_row)//2 + 1, (end_col + start_col)//2 +1 , end_row, end_col)


            return Node(-1,False, top_left, top_right, bottom_left, bottom_right)

        return create_tree(0,0, len(grid) - 1, len(grid[0]) - 1)