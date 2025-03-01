from collections import deque
# 用链表作为底层数据结构实现栈
# Python 的 deque 就是双链表
class MyLinkedStack:
    def __init__(self):
        self.list = deque()
    # 向栈顶加入元素，时间复杂度 O(1)
    def push(self, e):
        self.list.append(e)

    # 从栈顶弹出元素，时间复杂度 O(1)
    def pop(self):
        return self.list.pop()

    # 查看栈顶元素，时间复杂度 O(1)
    def peek(self):
        return self.list[-1]

    # 返回栈中的元素个数，时间复杂度 O(1)
    def size(self):
        return len(self.list)
# 用链表作为底层数据结构实现队列
# Python 的 deque 就是双链表
class MyLinkedQueue:
    def __init__(self):
        self.list = deque()

    # 向队尾插入元素，时间复杂度 O(1)
    def push(self, e):
        self.list.append(e)

    # 从队头删除元素，时间复杂度 O(1)
    def pop(self):
        return self.list.popleft()

    # 查看队头元素，时间复杂度 O(1)
    def peek(self):
        return self.list[0]

    # 返回队列中的元素个数，时间复杂度 O(1)
    def size(self):
        return len(self.list)

if __name__ == "__main__":
    queue = MyLinkedQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek()) # 1
    print(queue.pop()) # 1
    print(queue.pop()) # 2
    print(queue.peek()) # 3