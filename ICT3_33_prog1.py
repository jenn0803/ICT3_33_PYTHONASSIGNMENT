def product_or_sum(num1, num2):
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product

# Example usage
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

result = product_or_sum(n1, n2)
print("Result:", result)
