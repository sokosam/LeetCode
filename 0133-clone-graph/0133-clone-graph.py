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
        

        createdNodes = {}

        
        def dfs(createdNodes, node):
            if not node: return
            if  node.val in createdNodes and createdNodes[node.val][0]:
                return

            if node.val in createdNodes:
                newNode = createdNodes[node.val][1]
            else:
                newNode = Node(node.val, [])

            for i in node.neighbors:
                if i.val not in createdNodes:
                    newNeighbor = Node(i.val, [])
                    createdNodes[i.val] =  (False, newNeighbor)
                    newNode.neighbors.append(newNeighbor)
                else:
                    newNode.neighbors.append(createdNodes[i.val][1])
            createdNodes[node.val] = (True, newNode)
            for i in node.neighbors:
                dfs(createdNodes, i)

        dfs(createdNodes, node)
        if node and node.val:
            ans = createdNodes[node.val][1]
            return ans
        return None

        


