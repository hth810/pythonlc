class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针初始化指向 head
        slow, fast = head, head
        # 快指针走到末尾时停止
        while fast is not None and fast.next is not None:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
            # 快慢指针相遇，说明含有环
            if slow == fast:
                return True
        # 不包含环
        return False