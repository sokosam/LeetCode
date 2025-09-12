"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        pSeen = set()

        while p :

            if p.val == q.val:
                return q
            else:
                pSeen.add(p.val)
                p = p.parent
        

        while q :
            if q.val in pSeen:
                return q
            else:
                q = q.parent
