# Day 2: Data Structures
# Goal: List, Tuple, Set, and Dictionary

# LISTS (Ordered, Mutable)
# - Use lists to store an ordered collection of items.
# - Allows duplicates and supports various operations.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add an element at the end
numbers.remove(2)  # Remove specific element
numbers.insert(1, 99)  # Insert 99 at index 1
print(f"Updated List: {numbers}")

# Attributes & Best Practices:
# - Use clear names like `students_list`.
# - Use indexing to access or modify specific elements.
# - Lists are best for ordered and changeable data.

# TUPLES (Ordered, Immutable)
# - Use tuples for data that should not change.
# - Tuples are faster and memory-efficient compared to lists.
coordinates = (10, 20, 30)
print(f"Tuple Example: {coordinates}")

# Attributes & Best Practices:
# - Use tuples for fixed collections like (x, y, z) coordinates.
# - Add a trailing comma for single-item tuples: `single_item = (5,)`
# - Tuples ensure data integrity since they are immutable.

# SETS (Unordered, Unique Elements)
# - Use sets for collections that need unique elements.
# - Supports fast membership testing.
numbers_set = {1, 2, 3, 4}
numbers_set.add(5)  # Add a single element
numbers_set.update([6, 7, 8])  # Add multiple elements
numbers_set.discard(2)  # Remove an element (no error if not present)
print(f"Set Example: {numbers_set}")

# Attributes & Best Practices:
# - Use sets for deduplication of lists.
# - Use `set()` constructor for empty sets: `empty_set = set()`
# - Avoid indexing as sets are unordered.
# - Sets are efficient for checking membership.


# DICTIONARIES (Key-Value Pairs)
# - Use dictionaries to map keys to values.
# - Keys must be unique and immutable.
student = {
    "name": "Tahir",
    "age": 25,
    "language": "Python"
}
student["city"] = "Sukkur"  # Add new key-value pair
student["age"] = 26          # Update existing value
print(f"Student Dictionary: {student}")

# Attributes & Best Practices:
# - Use clear, descriptive keys: `student_data['age']`.
# - Use `dict.get()` to safely retrieve values with defaults.
# - Dictionaries are ideal for fast lookups and structured data.

# -----------------------------
# 5. Practice Examples:

# 1. List Practice: Add 3 new elements to a list and remove the second item.
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
numbers.pop(1)  # Remove the second item
print(f"List After Modification: {numbers}")

# 2. Tuple Practice: Store and print fixed coordinates.
coords = (100, 200, 300)
print(f"Coordinates: {coords}")

# 3. Set Practice: Create a set from a list (remove duplicates).
numbers = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers)
print(f"Unique Numbers Set: {numbers_set}")

# 4. Dictionary Practice: Update a dictionary with a new key-value pair.
student = {"name": "Tahir", "age": 25}
student["city"] = "Karachi"
print(f"Updated Student Dictionary: {student}")

# -----------------------------
# End of Data Structures Section
print("\n--- List, Tuple, Set, and Dictionary Explanation Complete ---")
