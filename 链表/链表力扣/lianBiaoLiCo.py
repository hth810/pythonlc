class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur=self.head
        for _ in range(index+1):
            cur=cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node=ListNode(val)
        temp=self.head.next
        temp.prev=node
        node.next=temp

        self.head.next=node
        node.prev=self.head
        self.size+=1

    def addAtTail(self, val: int) -> None:
        node=ListNode(val)
        temp=self.tail.prev
        temp.next=node
        node.prev=temp

        self.tail.prev=node
        node.next=self.tail
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        p=self.head
        for _ in range(index):
            p=p.next
        node=ListNode(val)
        node.next=p.next
        p.next.prev=node
        p.next=node
        node.prev=p
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p=self.head
        for _ in range(index):
            p=p.next
        p.next=p.next.next
        p.next.prev=p
        self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)