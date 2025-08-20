def mix_lists(list1, list2):
    # odd-index elements from list1 → index 1,3,5...
    odd_from_list1 = list1[1::2]
    
    # even-index elements from list2 → index 0,2,4...
    even_from_list2 = list2[0::2]
    
    # merge both
    result_list = odd_from_list1 + even_from_list2
    return result_list


# Example usage
list1 = [10, 20, 30, 40, 50, 60]
list2 = [70, 80, 90, 100, 110]

print("First List:", list1)
print("Second List:", list2)

result = mix_lists(list1, list2)
print("Result List:", result)