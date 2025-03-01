class LinearProbingHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.deleted = [False] * self.capacity

    def _hash(self, key):
        return key % self.capacity

    def insert(self, key, value):
        if self.size >= self.capacity or self.is_full():
            self._resize()

        index = self._hash(key)
        while (self.keys[index] is not None or self.deleted[index]) and (self.keys[index] != key):
            index = (index + 1) % self.capacity

        if self.keys[index] == key:
            self.values[index] = value  # Update existing key 修改
        else:
            self.keys[index] = key
            self.values[index] = value
            self.deleted[index] = False
            self.size += 1

    def search(self, key):
        index = self._hash(key)
        while (self.keys[index] is not None or self.deleted[index]):
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity

        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        while (self.keys[index] is not None or self.deleted[index]):
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.deleted[index] = True
                self.size -= 1
                self._rehash()
                return
            index = (index + 1) % self.capacity

        raise KeyError("Key not found")

    def _rehash(self):
        for i in range(self.capacity):
            if self.deleted[i]:
                index = (i + 1) % self.capacity
                while (self.keys[index] is not None and self.deleted[index]) or (index == i):
                    index = (index + 1) % self.capacity
                if index != i:
                    self.keys[index] = self.keys[i]
                    self.values[index] = self.values[i]
                    self.deleted[index] = self.deleted[i]
                    self.keys[i] = None
                    self.values[i] = None
                    self.deleted[i] = False

    def _resize(self):
        new_capacity = self.capacity * 2
        new_hash_table = LinearProbingHashTable(new_capacity)
        for i in range(self.capacity):
            if self.keys[i] is not None and not self.deleted[i]:
                new_hash_table.insert(self.keys[i], self.values[i])

        self.capacity = new_capacity
        self.keys = new_hash_table.keys
        self.values = new_hash_table.values
        self.deleted = new_hash_table.deleted

    def is_full(self):
        return self.size == self.capacity and all(not self.deleted[i] for i in range(self.capacity))

# Example usage:
hash_table = LinearProbingHashTable(10)
hash_table.insert(1, 'value1')
hash_table.insert(2, 'value2')
print(hash_table.search(1))  # Output: value1
hash_table.remove(1)
print(hash_table.search(1))  # Output: None