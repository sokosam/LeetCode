# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(ma, node): return 0 if not node else int(node.val >= ma) + dfs(max(ma,node.val), node.left) + dfs(max(ma,node.val), node.right)
        return dfs(root.val,root)

