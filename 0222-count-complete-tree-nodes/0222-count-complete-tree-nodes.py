# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lastLevel = None
        count = 0
        queue = deque()
        queue.append((root, 0))

        while queue:
            curr = queue.popleft()
            level = curr[1]
            node = curr[0]

            if lastLevel and level > lastLevel:
                break
            else:
                count += 1

            if node.left:
                queue.append((node.left, level + 1))
            elif not lastLevel:
                lastLevel = level  + 1
                print(lastLevel)

            if node.right:
                queue.append((node.right, level + 1))
            elif not lastLevel:
                lastLevel = level  + 1
                print(lastLevel)

        return count
        



