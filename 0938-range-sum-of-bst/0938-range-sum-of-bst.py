# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        q = deque()

        q.append(root)

        ans = 0
        while q:
            curr = q.popleft()
            if low <= curr.val <= high:
                ans += curr.val
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return ans