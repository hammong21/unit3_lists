"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""

def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Implementation: Uses list.insert(), which shifts all subsequent elements to the right.
    # Example: insert_at(fruits, 0, 'orange') makes 'orange' the new first element.
    # Performance: O(n) for inserts at beginning/middle (shifts needed), O(1) at end.
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Implementation: Uses list.pop(index), which shifts all subsequent elements to the left.
    # Why validation is important: Prevents IndexError crashes and improves robustness.
    # Performance: O(n) for deletes at beginning/middle (shifts needed), O(1) at end.
    if 0 <= index < len(lst):
        return lst.pop(index)
    else:
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Implementation: Scans list from index 0 to len(lst)-1, checking each element.
    # Why linear/sequential? Python lists are dynamic arrays—no direct hash lookup—so values must be checked one-by-one.
    # Performance: O(n) worst/average case; O(1) best case (first element).
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("Scenario: A fruit vendor is organizing a display. They start with a core set of fruits.")

    # Create a list of initial fruits (the core display).
    fruits = ['apple', 'banana', 'cherry']
    print(f"1. Initial fruit list: {fruits}")

    # Insert at the BEGINNING.
    print("\n   - Inserting 'orange' at the beginning (index 0)...")
    insert_at(fruits, 0, 'orange')
    print(f"   - Updated list: {fruits}")

    # Insert at the MIDDLE.
    print("\n   - Inserting 'grape' in the middle (index 2)...")
    insert_at(fruits, 2, 'grape')
    print(f"   - Updated list: {fruits}")

    # Insert at the END.
    print("\n   - Inserting 'kiwi' at the end (using insert method)...")
    insert_at(fruits, len(fruits), 'kiwi')
    print(f"   - Updated list: {fruits}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("Scenario: The vendor sells out of some fruits and needs to remove them from the display.")
    print(f"Current fruit list: {fruits}")

    # Delete from the BEGINNING.
    print("\n   - Deleting the first fruit (index 0)...")
    deleted_fruit = delete_at(fruits, 0)
    if deleted_fruit is not None:
        print(f"   - Removed fruit: {deleted_fruit}")
    else:
        print("   - Deletion failed: Invalid index.")
    print(f"   - Updated list: {fruits}")

    # Delete from the MIDDLE.
    print("\n   - Deleting the fruit in the middle (index 2)...")
    deleted_fruit = delete_at(fruits, 2)
    if deleted_fruit is not None:
        print(f"   - Removed fruit: {deleted_fruit}")
    else:
        print("   - Deletion failed: Invalid index.")
    print(f"   - Updated list: {fruits}")

    # Delete from the END.
    print("\n   - Deleting the last fruit (index len-1)...")
    deleted_fruit = delete_at(fruits, len(fruits) - 1)
    if deleted_fruit is not None:
        print(f"   - Removed fruit: {deleted_fruit}")
    else:
        print("   - Deletion failed: Invalid index.")
    print(f"   - Updated list: {fruits}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("Scenario: A customer is looking for specific fruits on the display.")
    print(f"Current fruit list: {fruits}")

    # Search for a value that EXISTS.
    print(f"\n   - Searching for 'apple'...")
    index = search_value(fruits, 'apple')
    if index != -1:
        print(f"   - Result: 'apple' was found at index {index}.")
    else:
        print("   - Result: 'apple' was not found in the list.")

    # Search for a value that does NOT exist.
    print(f"\n   - Searching for 'mango'...")
    index = search_value(fruits, 'mango')
    if index != -1:
        print(f"   - Result: 'mango' was found at index {index}.")
    else:
        print("   - Result: 'mango' was not found in the list (returns -1).")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("Scenario: Handling unusual or dangerous scenarios to ensure code robustness.")

    # Edge Case 1: Delete from an empty list
    print("\n   - Edge Case 1: Attempting to delete from an empty list.")
    empty_list = []
    print(f"   - Initial empty list: {empty_list}")
    print("   - Attempting to delete from index 0...")
    result = delete_at(empty_list, 0)
    if result is None:
        print("   - Correctly handled: Deletion from an empty list returned None (no crash).")
    else:
        print(f"   - Unexpected result: {result}")

    # Edge Case 2: Delete using an invalid index (out of range)
    print("\n   - Edge Case 2: Attempting to delete using an invalid index.")
    fruits = ['apple', 'banana', 'cherry']
    print(f"   - Current fruit list: {fruits}")
    invalid_index = 10
    print(f"   - Attempting to delete from index {invalid_index} (which is out of range)...")
    result = delete_at(fruits, invalid_index)
    if result is None:
        print("   - Correctly handled: Deletion at an invalid index returned None (no crash).")
    else:
        print(f"   - Unexpected result: {result}")


if __name__ == "__main__":
    main()