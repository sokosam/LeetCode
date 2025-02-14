# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        def delete(root):
            if not root:
                return None
            left = root.left
            right = root.right

            ans = right
            if not right:
                return left

            while right.left:
                right = right.left
            right.left = left
            return ans
        
        ans = root

        if not root or root.val == key:
            return delete(root)
        
        while root:
            if root.left and root.left.val == key:
                root.left = delete(root.left)
                break
            elif root.right and root.right.val == key:
                root.right = delete(root.right)
                break
            else:
                if key < root.val:
                    root = root.left
                else:
                    root = root.right
        return ans