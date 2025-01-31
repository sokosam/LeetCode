# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        s = []
        paths = []


        def dfs(root,s):
            if not root:return
            # print(root)
            s.append(root)
            if root in nodes:
                paths.append(s.copy())
            
            dfs(root.left, s)
            dfs(root.right,s)
            s.pop()
        
        dfs(root, s)




        # print(paths)
        
        # path1 = set(paths[0])
        # for i in range(len(paths[1]) -1, -1, -1):
        #     if paths[1][i] in path1:
        #         return paths[1][i]

        curr = None
        # current_val = -1
        # print(paths[0])
        for i in range(len(paths[0])):
            for k in range(len(paths)):
        
                if i >= len(paths[k]) or paths[k][i].val != paths[0][i].val:
                    return curr
            curr = paths[k][i]
        return curr