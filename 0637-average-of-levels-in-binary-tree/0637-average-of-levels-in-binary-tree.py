# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []

        def dfs(root, level):
            nonlocal levels
            if not root:
                return
            if (len(levels) == level):
                levels.append([root.val, 1])
            else:
                levels[level][0] += root.val
                levels[level][1] +=1
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return [i[0]/i[1] for i in levels]



