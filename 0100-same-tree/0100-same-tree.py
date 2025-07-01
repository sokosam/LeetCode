# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while q1 and q2:
            v1 = q1.popleft()
            v2 = q2.popleft()
            if not v1 and not v2:
                continue
            if not v1 or not v2:
                return False
            if v1.val != v2.val:
                return False            
            if v1:
                q1.append(v1.left)
                q1.append(v1.right)
                q2.append(v2.left)
                q2.append(v2.right)
        return True