from collections import OrderedDict

class LinkedHashMap(OrderedDict):
    def __init__(self, *args, **kwargs):
        super(LinkedHashMap, self).__init__(*args, **kwargs)

    def get(self, key, default=None):
        return super(LinkedHashMap, self).get(key, default)

    def put(self, key, value):
        super(LinkedHashMap, self).__setitem__(key, value)

    def remove(self, key):
        del self[key]

    def key_set(self):
        return self.keys()

    def values(self):
        return self.values()

    def entry_set(self):
        return [(key, self[key]) for key in self]

    def clear(self):
        super(LinkedHashMap, self).clear()

# Example usage:
linked_hash_map = LinkedHashMap()
linked_hash_map.put('key1', 'value1')
linked_hash_map.put('key2', 'value2')

print(linked_hash_map.get('key1'))  # Output: value1
print(linked_hash_map.key_set())    # Output: dict_keys(['key1', 'key2'])
print(linked_hash_map.values())    # Output: dict_values(['value1', 'value2'])
print(linked_hash_map.entry_set())  # Output: [('key1', 'value1'), ('key2', 'value2')]

linked_hash_map.remove('key1')
print(linked_hash_map.key_set())    # Output: dict_keys(['key2'])