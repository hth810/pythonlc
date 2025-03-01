class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head):
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)

        head.next.next = head

        head.next = None

        return last
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        p1,p2,p3=dummy,dummy,dummy
        for i in range(left-1):
            p1=p1.next

        l=p1.next
        for i in range(right):
            p2=p2.next
        r=p2.next
        p1.next=None
        p2.next=None
        p1.next=self.reverseList(l)
        while p3.next:
            p3=p3.next
        p3.next=r

        return dummy.next



