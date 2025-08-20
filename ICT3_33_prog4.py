def first_last_same(number_list):
    if len(number_list) == 0:
        return False   # if list is empty, return False
    
    return number_list[0] == number_list[-1]

# Example usage
numbers = [10, 20, 30, 10]
print("List:", numbers)
print("Result:", first_last_same(numbers))

numbers2 = [5, 6, 7, 8, 5]
print("List:", numbers2)
print("Result:", first_last_same(numbers2))

numbers3 = [1, 2, 3, 4]
print("List:", numbers3)
print("Result:", first_last_same(numbers3))
