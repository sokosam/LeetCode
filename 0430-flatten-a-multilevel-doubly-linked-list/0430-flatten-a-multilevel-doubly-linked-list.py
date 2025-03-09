"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        currNext = self.flatten(head.next)
        if head.child:
            newNext = self.flatten(head.child)
            tail = newNext
            while tail and tail.next:
                tail = tail.next

            if currNext:
                currNext.prev = tail
                tail.next = currNext
            head.next = newNext
            newNext.prev = head
            head.child = None
        return head

