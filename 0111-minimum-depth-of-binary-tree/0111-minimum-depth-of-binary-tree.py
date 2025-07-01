# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root, level):
            if not root:
                return float("inf")
            if not root.right and not root.left:
                return level

            return min(dfs(root.right, level + 1), dfs(root.left, level + 1))
        
        ans = dfs(root, 1)
        if ans != float('inf'):
            return ans
        return 0