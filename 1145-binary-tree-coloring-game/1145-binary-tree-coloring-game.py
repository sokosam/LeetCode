# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        

        redNode = [None]

        def countNodes(root):
            if not root:
                return 0

            if root.val ==x:
                redNode[0] = root
                return 0

            else:
                return 1 + countNodes(root.left) + countNodes(root.right)
        
        path1 = countNodes(root)
        path2 = countNodes(redNode[0].left)
        path3 = countNodes(redNode[0].right)

        return max(path1, path2,path3) > n//2
                # if root.val == x:
        #     return  countNodes(root.right) > n//2 or countNodes(root.left) > n//2 

        # q = deque()

        # q.append(root)
        # while q:
        #     curr = q.popleft()

        #     if curr.val == x:
        #         return countNodes(curr) <= n//2
            
        #     if curr.left:
        #         q.append(curr.left)
        #     if curr.right:
        #         q.append(curr.right)
        # return True
        
        # layer = 1

        # while 2**layer - 1 < n:
        #     layer += 1

        # nodes =