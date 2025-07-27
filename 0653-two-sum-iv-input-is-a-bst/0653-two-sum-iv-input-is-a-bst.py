# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def search(root, val):

            if not root:
                return False
            if root.val == val:
                return True
            
            if val > root.val:
                return search(root.right,val)
            else:
                return search(root.left,val)
        

        def dfs(node, k):
            if not node:
                return False
            nonlocal root
            found = search(root,k - node.val)
            return (found and 2*node.val != k) or dfs(node.left, k) or dfs(node.right, k)
        return dfs(root,k)
