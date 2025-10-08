# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        l = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        l.sort()
        l.reverse()
        def inorder2(root):
            if not root:
                return
            
            inorder2(root.left)
            root.val = l.pop()
            inorder2(root.right)
        inorder2(root)