# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """

               1
            2     3 
          4  5   6  7


        pre = 1 2 4 5 3 6 7
        in = 4 2 5 1 6 3 7

           2
         4   5

         pre = 2 4 5
         in  = 4 2 5

           3
         6   7

         pre = 3 6 7
         in  = 6 3 7

        """

        def helper(l, r, l2,r2, preorder,inorder):
            
            if r-l == 0:
                return TreeNode(preorder[l], None, None)
            elif r- l < 0: return None

            pivot = preorder[l]
            i = l2
            while inorder[i] != pivot:
                i +=1

            left_size = i - l2
            left = helper(l + 1, l + left_size, l2, i - 1, preorder, inorder)
            right = helper(l + left_size + 1, r, i + 1, r2, preorder, inorder)
            return TreeNode(pivot, left, right)
            
        # if len(preorder) == 1:
        #     return TreeNode(preorder[0], None, None)
        # elif len(preorder) == 0:
        #     return None

        # pivot = preorder[0]

        # i = 0
        # while inorder[i] != pivot:
        #     i += 1

        # left = self.buildTree(preorder[1:i + 1], inorder[0:i])
        # right = self.buildTree(preorder[i + 1 : ], inorder[i + 1:]) 

        # return TreeNode(pivot, left, right)
        return helper(0, len(inorder)- 1 , 0, len(inorder) -1 , preorder, inorder)

