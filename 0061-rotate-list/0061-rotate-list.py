# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        tail = head

        count = 0
        while temp:
            count += 1
            tail = temp
            temp= temp.next
        
        
        if k == 0:
            return head
        k %= count
        if k == 0:
            return head
        iterate = 0
        node = head

        while iterate < count - k - 1:
            iterate += 1
            node = node.next
        
        newHead = node.next
        print(newHead.val)
        node.next = None

        tail.next = head
        return newHead
