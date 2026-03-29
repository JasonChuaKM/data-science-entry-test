def find_and_replace[1, 2, 3, 4, 2, 2], 2, 5 :
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


def find_and_replace(lst, find_val, replace_val):
    """
    - Create a function that searches for all occurrences of a value (find_val)
      in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    # 1: Check if the input lst is actually a list using isinstance function
    # If it's not a list, return -1 as an error signal.
    if not isinstance(lst, list):
        return -1

    # Step 2: Go through the list using index positions.
    # We use range(len(lst)) to loop from index 0 to the end of the list.
    for i in range(len(lst)):

        # Step 3: Check if the current element matches the value we want to find.
        if lst[i] == find_val:

            # Step 4: If it matches, replace it with the new value.
            lst[i] = replace_val

    # Step 5: After all replacements are done, return the updated list.
    return lst

    



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

x = [1, 2, 3, 4, 2, 2], 2, 5
x.replace [2,5]
print(x)


x = ["apple", "banana", "apple"]
x.replace ["apple", "orange"]
print(x)
