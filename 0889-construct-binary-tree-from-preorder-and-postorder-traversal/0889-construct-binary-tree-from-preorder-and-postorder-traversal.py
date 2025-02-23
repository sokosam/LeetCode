# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


        """

               1
            2     3 
          4  5   6  7

          preorder = 1 2 4 5 3 6 7
         postorder = 4 5 2 6 7 3 1

        """

        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)
        elif len(preorder) == 0:
            return None
        # print(preorder, postorder)
        pivot = preorder[1]

        i = 0
        while postorder[i] != pivot:
            i += 1
        
        left = self.constructFromPrePost(preorder[1: i + 2], postorder[0: i + 1])
        right = self.constructFromPrePost(preorder[i+2:], postorder[i + 1: len(postorder) - 1])
        return TreeNode(preorder[0], left, right)
        