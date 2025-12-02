# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        tree1 = set()
        tree2 = set()

        def dfs(root, count):
            if not root:
                return

            count.add(root.val)
            dfs(root.left, count)
            dfs(root.right, count)
        dfs(root1, tree1)
        dfs(root2, tree2)
        for i in tree1:
            if target - i in tree2:
                return True
        for i in tree2:
            if target - i in tree1:
                return True
        return False

