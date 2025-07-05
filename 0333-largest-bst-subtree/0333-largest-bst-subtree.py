# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        """

                            4
                    2             7
                2       3      5
            2
        1 


                             4
                    1              6
                                5
                            2

        """
        ans = 0
        def dfs(root):
            nonlocal ans  
            if not root:
                return (0, float('inf'), float('-inf'))
            left = dfs(root.left)
            right = dfs(root.right)
            if left[2] < root.val <  right[1]:
                ans = max(ans, left[0] + right[0] + 1)
                newLeft = left[1]
                if newLeft == float('inf'):
                    newLeft = root.val
                newRight = right[2]
                if newRight == float('-inf'):
                    newRight = root.val
                return (left[0] + right[0] + 1, newLeft, newRight)
            else:
                return (-1, float('-inf'), float('inf'))
        dfs(root)
        return ans