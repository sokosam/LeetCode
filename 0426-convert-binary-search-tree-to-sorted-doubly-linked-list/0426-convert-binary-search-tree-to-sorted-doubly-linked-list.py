"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head = Node(None, None, None)
        curr = [head]
        end  = [None]
        def dfs(node, curr,end):
            if not node:
                return

            dfs(node.left,curr,end)

            curr[0].right = node
            node.left = curr[0]
            curr[0] = curr[0].right
            end[0] = curr[0]


            dfs(node.right, curr,end)
        dfs(root,curr,end)

        head.right.left = end[0]
        end[0].right = head.right
        return head.right

            