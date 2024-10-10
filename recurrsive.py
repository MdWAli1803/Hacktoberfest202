def find_min_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0], find_min_recursive(arr[1:]))

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value = find_min_recursive(array)
print(f"The minimum element in the array is: {min_value}")
