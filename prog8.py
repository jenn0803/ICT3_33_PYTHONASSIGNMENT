# Program to count occurrences of each element in a list
elements_input = input("Enter list elements separated by space: ")
elements = elements_input.split()

print("Original list:", elements)

count_dict = {}

for item in elements:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("The count dictionary is:", count_dict)
