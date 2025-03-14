# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        path = []
        def dfs(foundP,foundQ,p,q,level, root):
            if not root:
                return foundP, foundQ
            if foundP and foundQ:
                return True, True
            if root.val == p.val:
                foundP = True
            if root.val == q.val:
                foundQ = True
            
            before1, before2 = foundP,foundQ
            
            left1, left2 = dfs(foundP, foundQ, p,q, level + 1, root.left)
            right1, right2 = dfs(foundP,foundQ,p,q,level +1 , root.right)

            foundP= foundP or left1 or right1
            foundQ = foundQ or left2 or right2
            
            if foundP and foundQ:
                # print('hi', level, best[0], root)
                path.append(root)
            return foundP,foundQ
        dfs(False, False,p,q,0,root)
        

        foundp, foundq = False,False
        for i in path:
            if i == p:
                foundp = True
            if i == q:
                foundq = True
            if foundp and foundq:
                return i
        return path[0]
