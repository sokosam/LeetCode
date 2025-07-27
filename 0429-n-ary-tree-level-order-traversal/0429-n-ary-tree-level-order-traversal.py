"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        ans = []
        def traverse(root, level):
            if not root:
                return
            if len(ans) < level  + 1:
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            
            for i in root.children:
                traverse(i,level + 1)
        
        traverse(root,0)
        return ans
