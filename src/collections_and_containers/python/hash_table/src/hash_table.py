"""Module: hash_table
Provides a basic hash table implementation with separate chaining for collisions.
Includes HashTable class supporting add, remove, contains, size, clear operations,
and standard indexing access.
"""


class HashTable:
    def __init__(self, hash_func):
        """
        Initialize the HashTable with a given hash function.

        Parameters:
        hash_func (Callable): A function to compute hash values for keys.

        >>> ht = HashTable(lambda x: x)
        >>> isinstance(ht, HashTable)
        True
        """
        self.hash_func = hash_func
        self.buckets = [[] for _ in range(10)]
        self.num_items = 0

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.

        Parameters:
        key: The key to be added.
        value: The value associated with the key.

        >>> ht = HashTable(lambda x: x)
        >>> ht.add(1, 'one')
        >>> ht[1]
        'one'
        """
        bucket_index = self.hash_func(key) % len(self.buckets)
        for kv in self.buckets[bucket_index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.buckets[bucket_index].append([key, value])
        self.num_items += 1

    def remove(self, key):
        """
        Remove a key and its corresponding value from the hash table.

        Parameters:
        key: The key to be removed.

        Throws:
        Exception if the key is not found.

        >>> ht = HashTable(lambda x: x)
        >>> ht.add(1, 'one')
        >>> ht.remove(1)
        >>> ht.contains(1)
        False
        """
        bucket_index = self.hash_func(key) % len(self.buckets)
        for i, kv in enumerate(self.buckets[bucket_index]):
            if kv[0] == key:
                del self.buckets[bucket_index][i]
                self.num_items -= 1
                return
        raise Exception(f"Key {key} not found")

    def contains(self, key):
        """
        Check if a key is in the hash table.

        Parameters:
        key: The key to check for.

        Returns:
        bool: True if the key is found, False otherwise.

        >>> ht = HashTable(lambda x: x)
        >>> ht.add(1, 'one')
        >>> ht.contains(1)
        True
        >>> ht.contains(2)
        False
        """
        bucket_index = self.hash_func(key) % len(self.buckets)
        return any(kv[0] == key for kv in self.buckets[bucket_index])

    def size(self):
        """
        Return the number of key-value pairs in the hash table.

        Returns:
        int: The number of key-value pairs.

        >>> ht = HashTable(lambda x: x)
        >>> ht.add(1, 'one')
        >>> ht.add(2, 'two')
        >>> ht.size()
        2
        """
        return self.num_items

    def clear(self):
        """
        Clear all key-value pairs from the hash table.

        >>> ht = HashTable(lambda x: x)
        >>> ht.add(1, 'one')
        >>> ht.clear()
        >>> ht.size()
        0
        """
        self.buckets = [[] for _ in range(10)]
        self.num_items = 0

    def __getitem__(self, key):
        """
        Access the value associated with a given key.

        Parameters:
        key: The key to access.

        Returns:
        The value associated with the key.

        Throws:
        Exception if the key is not found.

        >>> ht = HashTable(lambda x: x)
        >>> ht.add(1, 'one')
        >>> ht[1]
        'one'
        """
        bucket_index = self.hash_func(key) % len(self.buckets)
        for kv in self.buckets[bucket_index]:
            if kv[0] == key:
                return kv[1]
        raise Exception(f"Key {key} not found")

    def __setitem__(self, key, value):
        """
        Set the value for a given key in the hash table.

        Parameters:
        key: The key for which to set the value.
        value: The value to set.

        >>> ht = HashTable(lambda x: x)
        >>> ht[1] = 'one'
        >>> ht[1]
        'one'
        """
        self.add(key, value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
