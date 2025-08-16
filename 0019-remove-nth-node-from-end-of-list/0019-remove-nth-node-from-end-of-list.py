# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(root):

            prev = None
            curr = root

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr= next
            return prev


        root = reverse(head)
        curr = root
        prev = None
        count = 1

        while count != n:
            prev = curr
            curr = curr.next
            count +=1
        if prev:
            prev.next = curr.next
        else:
            root = curr.next



        return reverse(root) 