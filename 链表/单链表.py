class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(arr: 'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None

    head=ListNode(arr[0])
    cur=head
    for i in range(1,len(arr)):
        cur.next=ListNode(arr[i])
        cur=cur.next

    return head
#查
head=createLinkedList([1,2,3,4,5])
p=head
while p != None:
    print(p.val)
    p=p.next

#增
head=createLinkedList([1,2,3,4,5])
newHead=ListNode(0)
newHead.next=head
head=newHead

#尾部插入
head=createLinkedList([1,2,3,4,5])
p=head
while p.next.val != None:
    p=p.next

p.next=ListNode(6)

#中间插入
head=createLinkedList([1,2,3,4,5])
p=head
for _ in range(2):
    p=p.next
new_Node=ListNode(66)
new_Node.next=p.next
p.next=new_Node

#删除
head=createLinkedList([1,2,3,4,5])
p=head
for _ in range(2):
    p=p.next
p.next=p.next.next

#删尾部
head = createLinkedList([1, 2, 3, 4, 5])
# 删除尾节点
p = head
# 找到倒数第二个节点
while p.next.next is not None:
    p = p.next
# 此时 p 指向倒数第二个节点
# 把尾节点从链表中摘除
p.next = None

#在单链表头部删除元素
head = createLinkedList([1, 2, 3, 4, 5])
# 删除头结点
head = head.next


