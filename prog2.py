# Iterate through first 10 numbers (0–9)
previous_num = 0

print("Printing sum of current and previous number in the range(10):")
for current_num in range(10):
    sum_nums = previous_num + current_num
    print(f"Current Number: {current_num}, Previous Number: {previous_num}, Sum: {sum_nums}")
    previous_num = current_num
