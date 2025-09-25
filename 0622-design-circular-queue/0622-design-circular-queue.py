class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.start = Node(-1)
        self.end = Node(-1)
        self.start.next = self.end
        self.start.prev = self.end
        self.end.next =self.start
        self.end.prev = self.start
        self.size = k

        

    def enQueue(self, value: int) -> bool:
        if self.size == 0:
            return False

        node = Node(value)
        nextNode = self.end.next

        nextNode.prev = node
        self.end.next = node
        node.next = nextNode
        node.prev = self.end
        self.size -=1
        return True


    def deQueue(self) -> bool:

        if self.start.prev == self.end:
            return False
        
        deletedNode = self.start.prev

        deletedNode.prev.next = self.start
        self.start.prev = deletedNode.prev
        self.size +=1
        return True
        

    def Front(self) -> int:

        if self.start.prev == self.end:
            return -1
        return self.start.prev.value
        

    def Rear(self) -> int:
        if self.start.prev == self.end:
            return -1
        return self.end.next.value
    def isEmpty(self) -> bool:
        return self.start.prev == self.end
    def isFull(self) -> bool:
        return self.size == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()