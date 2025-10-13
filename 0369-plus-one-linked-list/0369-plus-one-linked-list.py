# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverse(node):
            prev = None
            while node:
                nextNode = node.next
                node.next = prev
                prev = node
                node = nextNode
            return prev

        head = reverse(head)
        start = head
        prev = None

        while head and head.val + 1 == 10:
            head.val = 0
            prev= head
            head = head.next
            
        
        if not head:
            new = ListNode(1)
            prev.next = new
            head = new
        else:
            head.val +=1
        
        head = reverse(start)
        return head

