# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:


        q = deque()
        q.append([root, 1])
        
        cur = 0
        while q:
            curr = q.popleft()
            node = curr[0]
            level = curr[1]

            if level != cur + 1:
                return False
            
            if node.left:
                q.append([node.left, 2*level])
            if node.right:
                q.append([node.right, 2*level + 1])
            cur = level
        return True

