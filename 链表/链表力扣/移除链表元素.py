class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        while pre.next:
            if pre.next.val==val:
                pre.next=pre.next.next
            else:
                pre=pre.next
        return dummy.next