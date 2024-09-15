#Write a Python function that takes a list and returns a new list with distinct elements from the first list

def distinct_elements(lst):
    return list(set(lst))

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
print("Distinct elements:", distinct_elements(lst))