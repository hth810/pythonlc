from typing import Optional


class DoublyListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def createDoublyLinkedList(arr: 'List[int]') -> Optional[DoublyListNode]:
    if not arr: return None

    head=DoublyListNode(arr[0])
    cur=head
    for val in arr[1:]:
        new_node=DoublyListNode(val)
        cur.next=new_node
        new_node.prev=cur
        cur=cur.next

    return head

#在双链表头部插入新元素
head = createDoublyLinkedList([1, 2, 3, 4, 5])
# 在双链表头部插入新节点 0
new_head = DoublyListNode(0)
new_head.next = head
head.prev = new_head
head = new_head

# 在双链表中删除一个节点
head = createDoublyLinkedList([1, 2, 3, 4, 5])
# 删除第 4 个节点
# 先找到第 3 个节点
p = head
for i in range(2):
    p = p.next
# 现在 p 指向第 3 个节点，我们将它后面的那个节点摘除出去
toDelete = p.next
# 把 toDelete 从链表中摘除
p.next = toDelete.next
toDelete.next.prev = p
# 把 toDelete 的前后指针都置为 null 是个好习惯（可选）
toDelete.next = None
toDelete.prev = None
