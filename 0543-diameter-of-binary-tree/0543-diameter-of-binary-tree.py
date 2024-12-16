# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        trueMax = 0
        def dfs(root, level):
            nonlocal trueMax
            if not root:
                return level - 1
            
            left = dfs(root.left, level + 1) 
            right = dfs(root.right, level + 1)
            trueMax = max(trueMax, left + right - 2*level)
            return max(left, right)

        if not root: return 0 
        
        right = dfs(root.right, 1)
        left = dfs(root.left, 1)

        return max(right + left, trueMax)
