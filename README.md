# PersonalDictionary (Custom HashMap Implementation in Python)
## Why this project

Part of a CS fundamentals learning path: helps internalize hashing, collision resolution, and linked list manipulation. Good practice for algorithm interviews and systems thinking.

## Overview
This project is a **custom implementation of a HashMap** in Python, built from scratch for learning purposes.  
It uses:
- A **simple hash function** (sum of ASCII codes).
- A list of **buckets**, where each bucket is a `LinkedList` that handles collisions via chaining.
- Each node in the linked list stores a `(key, value)` pair (implemented as `node.key` and `node.value`).

The goal is to simulate how `dict` / hash maps work internally while practicing data structures: hashing, linked lists, collision handling and basic hashing operations.

---

## Current behavior
- `addToDictionary(key, value)` — Inserts the `(key, value)` pair. If the key already exists in the bucket, **the existing value is updated** (first matching node is replaced). If the key does not exist, a new node is inserted. This makes the current API behave like a standard HashMap (single-value per key).
- `getValue(key)` — Returns a list with the value(s) found for the key (usually a single value with the current design).
- `removeKey(key)` — Removes all nodes that match the given key; if the bucket becomes empty, the bucket is removed from the bucket list.
- `__str__` — Visualizes buckets and `(key, value)` entries for debugging.
- Collision handling via chaining with linked lists.

---

## Features Implemented
- `HashFunction(string) -> int` (sum of ASCII codes)
- `addToDictionary(key, value)` (insert/update)
- `getValue(key)` (lookup)
- `removeKey(key)` (delete key from buckets)
- `updateKeyInDictionary` (helper used to overwrite existing key)
- `__str__` for visualization
- Unit tests covering common scenarios

---

## Example usage

```python
from PersonalDictionary import PersonalDictionary

myDict = PersonalDictionary()

myDict.addToDictionary("ab", 4)
myDict.addToDictionary("ab", 5)  # updates the existing "ab" entry -> new value 5
myDict.addToDictionary("ba", 8)  # "ab" and "ba" collide with current hash function

print(myDict.getValue("ab"))   # [5]
print(myDict.getValue("ba"))   # [8]

myDict.removeKey("ab")
# myDict.getValue("ab") -> raises IndexError
print(myDict)
```

## Unit tests

A small test suite (test.py) has been added using Python unittest covering:

- `Insert & lookup

- `Remove existing / non-existing keys

- `Hash function correctness

- `Update behavior

- `Run tests:
```python
python -m unittest
# or
python -m unittest test.py
```

## Notable bugs fixed

Fixed a bug where deleting nodes could leave an empty bucket object in the bucket list; later lookups tried to access .head.key on an empty bucket and crashed.
Solution: after deleting, if bucket.head is None, remove the bucket itself from listOfObj.
