# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if slow == fast:
            return head
        else:
            prev.next = None
            left = self.sortList(head)
            right = self.sortList(slow)

            newHead = None
            curr = None
            while left and right:
                if not newHead:
                    if left.val < right.val:
                        newHead = left
                        left = left.next
                        curr = newHead
                    else:
                        newHead = right
                        right = right.next
                        curr = newHead
                else:
                    if left.val < right.val:
                        curr.next = left
                        left = left.next
                        curr = curr.next
                    else:
                        curr.next = right
                        curr = curr.next
                        right = right.next
            while left:
                curr.next = left
                curr = curr.next
                left = left.next
            while right:
                curr.next = right
                curr = curr.next
                right = right.next
        return newHead

