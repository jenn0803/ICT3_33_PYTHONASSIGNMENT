def even_index_chars(input_str):
    print("Original string:", input_str)
    print("Characters at even index positions:")
    for i in range(0, len(input_str), 2):   # step=2 → even index only
        print(input_str[i])

# Example usage
text = input("Enter a string: ")
even_index_chars(text)
