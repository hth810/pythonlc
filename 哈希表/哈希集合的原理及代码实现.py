class HashSet:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.empty = None
        self.deleted = object()

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [self.empty] * self.capacity
        self.size = 0
        for bucket in old_buckets:
            if bucket is not self.deleted and bucket is not self.empty:
                self.add(bucket)

    def add(self, key):
        if self.size >= self.capacity * 0.7:
            self._resize()

        index = self._hash(key)
        first_deleted = None
        while True:
            if self.buckets[index] is self.empty:
                if first_deleted is not None:
                    index = first_deleted
                self.buckets[index] = key
                self.size += 1
                return
            elif self.buckets[index] is self.deleted:
                if first_deleted is None:
                    first_deleted = index
            elif self.buckets[index] == key:
                return
            index = (index + 1) % self.capacity

    def search(self, key):
        index = self._hash(key)
        while True:
            if self.buckets[index] is self.empty:
                return False
            elif self.buckets[index] is self.deleted:
                pass
            elif self.buckets[index] == key:
                return True
            else:
                return False
            index = (index + 1) % self.capacity

    def remove(self, key):
        index = self._hash(key)
        while True:
            if self.buckets[index] is self.empty:
                raise KeyError("Key not found")
            elif self.buckets[index] is self.deleted:
                pass
            elif self.buckets[index] == key:
                self.buckets[index] = self.deleted
                self.size -= 1
                return
            index = (index + 1) % self.capacity


# Example usage:
hash_set = HashSet()
hash_set.add('apple')
hash_set.add('banana')
print(hash_set.search('apple'))  # Output: True
print(hash_set.search('cherry'))  # Output: False
hash_set.remove('apple')
print(hash_set.search('apple'))  # Output: False