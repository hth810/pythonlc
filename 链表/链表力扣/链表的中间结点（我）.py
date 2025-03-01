class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        count=0
        while p:
            p=p.next
            count+=1
        if count%2==0:
            for _ in range(count//2):
                dummy=dummy.next
            return dummy
        for _ in range((count+1)//2):
            dummy=dummy.next
        return dummy