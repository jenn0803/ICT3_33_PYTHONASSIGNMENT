def modify_list(lst):
    # remove element at index 4
    element = lst.pop(4)

    # insert it at 2nd position (index 1, since index starts at 0)
    lst.insert(1, element)

    # append it at the end
    lst.append(element)

    return lst


# Example usage
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Original List:", numbers)

result = modify_list(numbers)
print("Modified List:", result)
