# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """

               1
            2     3 
          4  5   6  7

          inorder = 4 2 5 1 6 3 7
        postorder = 4 5 2 6 7 3 1


        """

        # def helper()

        if len(inorder) == 1:
            return TreeNode(inorder[0],None,None)
        elif len(inorder) == 0:
            return None

        pivot = postorder[-1]

        i = 0
        while inorder[i] != pivot:
            i += 1
        
        left = self.buildTree(inorder[0: i], postorder[0: i])
        right = self.buildTree(inorder[i +1:], postorder[i: len(postorder) -1])

        return TreeNode(pivot, left, right)