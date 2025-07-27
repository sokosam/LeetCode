# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def search(root, level):

            if not root:
                return
            
            if len(ans) < level + 1:
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            search(root.left,level +1)
            search(root.right, level+1)
        search(root,0)
        return ans
