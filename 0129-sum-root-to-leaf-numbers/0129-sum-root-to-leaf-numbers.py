# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        q  = deque()

        q.append((root,0, 0))

        ans = 0
        while q:
            curr, exp, total = q.popleft()
            total*= 10
            total += curr.val   
            if not curr.right and not curr.left:
                ans += total
            if curr.right:
                q.append((curr.right, exp + 1, total))
            
            if curr.left:
                q.append((curr.left, exp + 1, total))
            
        return ans