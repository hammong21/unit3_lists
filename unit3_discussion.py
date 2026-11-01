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
    # Implementation: Uses list.insert() to place the new post at the given index.
    # Example: insert_at(posts, 0, new_post) adds a new post to the top of the timeline.
    # Performance: O(n) for inserts at beginning/middle (shifts required), O(1) at end.
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
    # Implementation: Uses list.pop(index) to remove and return the post.
    # Why validation is important: Prevents IndexError crashes during post deletion.
    # Performance: O(n) for deletions at beginning/middle (shifts required), O(1) at end.
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
    # Implementation: Scans list from index 0 to len(lst)-1, checking each post.
    # Why linear/sequential? Python lists are dynamic arrays—no direct hash lookup—so posts must be checked one-by-one.
    # Performance: O(n) worst/average case; O(1) best case (first post matches).
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
    print("Scenario: A user opens their social media timeline. New posts appear at different positions.")

    # Create a list of initial posts (the user's timeline).
    posts = ["Post 1: Morning coffee!", "Post 2: Weekend hike", "Post 3: Birthday party"]
    print(f"1. Initial timeline: {posts}")

    # Insert at the BEGINNING (new post at top of timeline).
    print("\n   - Inserting 'New post: Just launched!' at the beginning (index 0)...")
    insert_at(posts, 0, "New post: Just launched!")
    print(f"   - Updated timeline: {posts}")

    # Insert at the MIDDLE.
    print("\n   - Inserting 'Midday update' in the middle (index 2)...")
    insert_at(posts, 2, "Midday update")
    print(f"   - Updated timeline: {posts}")

    # Insert at the END (append to bottom of timeline).
    print("\n   - Inserting 'Evening thoughts' at the end (index len(posts))...")
    insert_at(posts, len(posts), "Evening thoughts")
    print(f"   - Updated timeline: {posts}")


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
    print("Scenario: The user decides to delete some posts from their timeline.")
    print(f"Current timeline: {posts}")

    # Delete from the BEGINNING (oldest visible post near top).
    print("\n   - Deleting the post at the top (index 0)...")
    deleted_post = delete_at(posts, 0)
    if deleted_post is not None:
        print(f"   - Removed post: {deleted_post}")
    else:
        print("   - Deletion failed: Invalid index.")
    print(f"   - Updated timeline: {posts}")

    # Delete from the MIDDLE.
    print("\n   - Deleting the post in the middle (index 2)...")
    deleted_post = delete_at(posts, 2)
    if deleted_post is not None:
        print(f"   - Removed post: {deleted_post}")
    else:
        print("   - Deletion failed: Invalid index.")
    print(f"   - Updated timeline: {posts}")

    # Delete from the END.
    print("\n   - Deleting the last post (index len-1)...")
    deleted_post = delete_at(posts, len(posts) - 1)
    if deleted_post is not None:
        print(f"   - Removed post: {deleted_post}")
    else:
        print("   - Deletion failed: Invalid index.")
    print(f"   - Updated timeline: {posts}")


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
    print("Scenario: The user searches for a specific post using keywords.")
    print(f"Current timeline: {posts}")

    # Search for a value that EXISTS.
    search_post = "Midday update"
    print(f"\n   - Searching for '{search_post}'...")
    index = search_value(posts, search_post)
    if index != -1:
        print(f"   - Result: '{search_post}' was found at index {index}.")
    else:
        print("   - Result: '{search_post}' was not found in the list.")

    # Search for a value that does NOT exist.
    search_post = "Urgent update"
    print(f"\n   - Searching for '{search_post}'...")
    index = search_value(posts, search_post)
    if index != -1:
        print(f"   - Result: '{search_post}' was found at index {index}.")
    else:
        print(f"   - Result: '{search_post}' was not found in the list (returns -1).")


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
    print("\n   - Edge Case 1: Attempting to delete from an empty timeline.")
    empty_timeline = []
    print(f"   - Initial empty timeline: {empty_timeline}")
    print("   - Attempting to delete from index 0...")
    result = delete_at(empty_timeline, 0)
    if result is None:
        print("   - Correctly handled: Deletion from an empty list returned None (no crash).")
    else:
        print(f"   - Unexpected result: {result}")

    # Edge Case 2: Delete using an invalid index (out of range)
    print("\n   - Edge Case 2: Attempting to delete using an invalid index.")
    posts = ["Post 1: Morning coffee!", "Post 2: Weekend hike", "Post 3: Birthday party"]
    print(f"   - Current timeline: {posts}")
    invalid_index = 10
    print(f"   - Attempting to delete from index {invalid_index} (which is out of range)...")
    result = delete_at(posts, invalid_index)
    if result is None:
        print("   - Correctly handled: Deletion at an invalid index returned None (no crash).")
    else:
        print(f"   - Unexpected result: {result}")


if __name__ == "__main__":
    main()