# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

            
        ans = 1
        queue = deque()
        queue.append((root,1, 1))
        m = {}

        while queue:
            val = queue.popleft()
            node = val[0]
            index = val[1]
            level = val[2]

            if level not in m:
                m[level] = [index, index]
            else:
                m[level] = [min(index,m[level][0]), max(index,m[level][1])]
            ans = max(ans, m[level][1] - m[level][0]+ 1)

            if node.left:
                queue.append((node.left, 2*index, level + 1))
            if node.right:
                queue.append((node.right, 2*index + 1, level + 1))
        return ans






        
            