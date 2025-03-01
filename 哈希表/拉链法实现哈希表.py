class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * self.size
    # Hash function
    def _hash(self, key):
        return hash(key) % self.size
    # Insertion
    def insert(self, key, value):
        index = self._hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = HashNode(key, value)
        else:
            prev = None
            while node is not None:
                if node.key == key:
                    node.value = value  # Update existing key
                    return
                prev = node
                node = node.next
            prev.next = HashNode(key, value)

    def search(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:
                    self.buckets[index] = node.next
                else:
                    prev.next = node.next
                return node.value
            prev = node
            node = node.next
        return None  # Key not found

# Example usage:
ht = HashTable(10)
ht.insert('key1', 'value1')
ht.insert('key2', 'value2')
print(ht.search('key1'))  # Output: value1
ht.remove('key1')
print(ht.search('key1'))  # Output: None