def slice_and_reverse(lst):
    # Find chunk size (length must be divisible by 3)
    chunk_size = len(lst) // 3
    
    # Slice into 3 chunks
    chunk1 = lst[0:chunk_size]
    chunk2 = lst[chunk_size:2*chunk_size]
    chunk3 = lst[2*chunk_size:]
    
    # Reverse each chunk
    return [chunk1[::-1], chunk2[::-1], chunk3[::-1]]


# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original List:", numbers)
result = slice_and_reverse(numbers)
print("Chunks Reversed:", result)
