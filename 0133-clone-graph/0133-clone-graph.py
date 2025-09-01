"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
        
        m = {}

        def helper(node):
            if not node:
                return None
            if node.val in m and len(m[node.val].neighbors) > 0:
                return
            
            copy = Node(node.val, [])
            neighbors = []
            if node.val in m:
                copy = m[node.val]

            for adj in node.neighbors:
                if adj.val in m:
                    neighbors.append(m[adj.val])
                else:
                    shallow = Node(adj.val, [])
                    neighbors.append(shallow)
                    m[adj.val] = shallow
            
            copy.neighbors = neighbors
            m[node.val] = copy

            for adj in node.neighbors:
                helper(adj)
        
        helper(node)
        if len(m) == 0:
            return None
        return m[1]