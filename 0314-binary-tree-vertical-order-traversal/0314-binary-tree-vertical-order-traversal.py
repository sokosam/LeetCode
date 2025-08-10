# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        left = []
        right = []
        middle = []

        q = deque()
        q.append([root, 0])

        while q:
            curr = q.popleft()

            if curr[1] == 0:
                middle.append(curr[0].val)
            elif curr[1] < 0:
                rng = abs(curr[1])
                if len(left) < rng:
                    left.append([])
                left[rng - 1].append(curr[0].val)
            else:
                rng = curr[1]
                if len(right) < rng:
                    right.append([])
                right[rng - 1].append(curr[0].val)

            if curr[0].left:
                q.append([curr[0].left, curr[1] - 1])
            if curr[0].right:
                q.append([curr[0].right, curr[1] + 1])
        left.reverse()
        return left + [middle] + right                
