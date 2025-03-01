import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 将优先级和元素一起放入队列，优先级高的排在前面
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 弹出优先级最高的元素
        return heapq.heappop(self._queue)[-1] if self._queue else None

    def is_empty(self):
        return len(self._queue) == 0

# 使用示例
pq = PriorityQueue()
pq.push('task1', 1)
pq.push('task2', 2)
pq.push('task3', 3)

while not pq.is_empty():
    task = pq.pop()
    print(task)