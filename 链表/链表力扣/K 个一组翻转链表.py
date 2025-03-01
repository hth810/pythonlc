class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head,k):
        pre,cur=None,head
        for _ in range(k):
            cur.next,pre,cur=pre,cur,cur.next
        return pre,head
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next:
            cur=p.next
            for i in range(k):
                if not cur:
                    return dummy.next
                cur=cur.next
            p.next,p=self.reverseList(p.next,k)
            p.next=cur
        return dummy.next

            