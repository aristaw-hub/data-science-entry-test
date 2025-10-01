def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is actually a list
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    
    # Create a new list with replacements
    result = []
    for item in lst:
        if item == find_val:
            result.append(replace_val)
        else:
            result.append(item)
    
    return result

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# Scenario 1: Replace all occurrences of 2 with 5
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Scenario 1:", result1)
# Output: [1, 5, 3, 4, 5, 5]

# Scenario 2: Replace all occurrences of "apple" with "orange"
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Scenario 2:", result2)

# Output: ['orange', 'banana', 'orange']
