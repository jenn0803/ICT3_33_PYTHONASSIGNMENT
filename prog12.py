numbers = [10,20,33,46,55,75,150,180,200]

print("number divisible by 5 (stop if?150):")

for num in numbers:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)