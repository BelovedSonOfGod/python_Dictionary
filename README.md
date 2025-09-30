# PersonalDictionary (Custom HashMap Implementation in Python)

## Overview
This project is a **custom implementation of a HashMap** in Python, built from scratch for learning purposes.  
It uses:
- A **simple hash function** (sum of ASCII codes).
- A list of **buckets**, where each bucket is a `LinkedList` that handles collisions.
- Each node in the linked list stores a `(key, value)` pair.

The goal is to simulate how dictionaries (`dict`) and hash maps work internally, while practicing data structures like linked lists and collision handling.

---

## Features Implemented ✅
- **Custom hash function**: `HashFunction(string) → int`  
- **Insert (`addToDictionary`)**: Adds a `(key, value)` pair to the hash map.  
  - If the key is new → create a new bucket (LinkedList).  
  - If the key collides → add to the existing bucket.  
- **Search (`getValue`)**: Retrieves all values associated with a given key.  
- **Remove (`removeKey`)**: Deletes all entries associated with a given key.  
- **Collision handling**: Implemented via **chaining with linked lists**.

---

## Planned Improvements 📝
- **Update (`updateValue`)**:  
  Add a method that replaces the existing value for a given key (like a real HashMap), instead of always appending.  
- **Cleanup empty buckets**:  
  After `removeKey`, if a bucket becomes empty, remove it from the list.  
- **Better printing/debugging**:  
  Add `__str__` or `__repr__` methods to visualize the internal state (buckets and chains).  

---

## Example Usage

```python
from PersonalDictionary import PersonalDictionary

myDict = PersonalDictionary()

# Insert values
myDict.addToDictionary("ab", 4)
myDict.addToDictionary("ab", 5)
myDict.addToDictionary("ba", 8)   # Collides with "ab" (same hash)

# Retrieve values
print(myDict.getValue("ab"))   # [4, 5]
print(myDict.getValue("ba"))   # [8]

# Remove values
myDict.removeKey("ab")
print(myDict.getValue("ab"))   # Raises IndexError
Roadmap
 Basic HashMap with insert & collisions

 LinkedList integration per bucket

 getValue and removeKey

 Implement updateValue (real HashMap behavior)
