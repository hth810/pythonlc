#队列
class MyQueue:
    def __init__(self):
        self.queue = []
    def push(self, e):
        """向队尾插入元素，时间复杂度 O(1)"""
        self.queue.append(e)
    def pop(self):
        """从队头删除元素，时间复杂度 O(1)"""
        if self.size() == 0:
            raise IndexError("pop from an empty queue")
        return self.queue.pop(0)
    def peek(self):
        """查看队头元素，时间复杂度 O(1)"""
        if self.size() == 0:
            raise IndexError("peek from an empty queue")
        return self.queue[0]
    def size(self):
        """返回队列中的元素个数，时间复杂度 O(1)"""
        return len(self.queue)

#栈
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        """向栈顶插入元素，时间复杂度 O(1)"""
        self.stack.append(e)

    def pop(self):
        """从栈顶删除元素，时间复杂度 O(1)"""
        if self.size() == 0:
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """查看栈顶元素，时间复杂度 O(1)"""
        if self.size() == 0:
            raise IndexError("peek from an empty stack")
        return self.stack[-1]

    def size(self):
        """返回栈中的元素个数，时间复杂度 O(1)"""
        return len(self.stack)