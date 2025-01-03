"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}


        def helper(curr, nodeMap):
            if not curr: return curr
            if curr in nodeMap:
                return nodeMap[curr]

            newNode = Node(curr.val, None, None )
            nodeMap[curr] = newNode
            nodeMap[curr].next = helper(curr.next, nodeMap)
            nodeMap[curr].random =helper(curr.random, nodeMap)
            return newNode

        ans =helper(head, nodeMap)
        return ans