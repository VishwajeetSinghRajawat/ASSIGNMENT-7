def remove_duplicates(nums):
    return list(set(nums))


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


# Example usage
unique_array = [4, 5, 2, 4, 5, 6, 5, 4, 5, 5, 6]

# Remove duplicates
input_array = remove_duplicates(unique_array)
print("Input array:", input_array)

# Sort using selection sort
sorted_array_selection = selection_sort(input_array)
print("Sorted array (Selection Sort):", sorted_array_selection)

# Sort using bubble sort
sorted_array_bubble = bubble_sort(input_array)
print("Sorted array (Bubble Sort):", sorted_array_bubble)
