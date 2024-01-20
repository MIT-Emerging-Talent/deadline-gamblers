
# Hash Table Implementation

## Overview

This module, `hash_table.py`, provides a basic implementation of a hash table using separate chaining for collision resolution. The `HashTable` class is designed to be flexible with customizable hash functions and supports standard hash table operations.

## Demo

- **Custom Hash Function**: Users can define their own hash function.
- **Basic Operations**: Includes `add`, `remove`, `contains`, and `size`.
- **Pythonic Access**: Supports using the `[]` operator for getting and setting values.
- **Collision Handling**: Implements separate chaining for collision resolution.
- **Dynamic Key Support**: Can handle various data types as keys (e.g., integers, strings).

## Implementation Details

- **Separate Chaining**: Each bucket in the hash table is a list, allowing multiple key-value pairs in the same bucket.
- **Hash Function Flexibility**: Users pass a hash function to the constructor. This function is used to determine the bucket index for each key.
- **Automatic Resizing**: Not implemented; the size of the hash table is fixed at initialization.

## Usage

### Basic Operations

1. **Adding Elements**
   ```python
   from hash_table import HashTable

   hash_table = HashTable(lambda x: x)
   hash_table.add(1, "one")
   hash_table.add(2, "two")
   ```

2. **Accessing Elements**
   ```python
   print(hash_table[1])  # Output: one
   ```

3. **Removing Elements**
   ```python
   hash_table.remove(2)
   ```

4. **Checking for Key Existence**
   ```python
   print(hash_table.contains(2))  # Output: False
   ```

5. **Getting the Size**
   ```python
   print(hash_table.size())  # Output: 1 (after removing key 2)
   ```

### Use Cases

1. **Storing User Information**
   ```python
   user_table = HashTable(lambda x: x)
   user_table.add(1001, {"name": "Alice", "email": "alice@example.com"})
   user_table.add(1002, {"name": "Bob", "email": "bob@example.com"})

   user_id = 1001
   if user_table.contains(user_id):
       print(f"User Details: {user_table[user_id]}")
   ```

2. **Caching Computed Results**
   ```python
   computation_cache = HashTable(lambda x: x)

   def get_computation(n):
       if not computation_cache.contains(n):
           result = sum(i*i for i in range(n))
           computation_cache.add(n, result)
           return result, "Computed"
       return computation_cache[n], "Cached"

   print(get_computation(10))  # Computed on first call
   print(get_computation(10))  # Cached on subsequent calls
   ```
## Testing:
- Run the following command line in the directory `hash_table`
```pash
python -m unittest discover -v
```
## Conclusion

This `HashTable` implementation provides a straightforward and flexible approach to using hash tables in Python, suitable for various applications where quick data access, storage, and retrieval are essential.
