def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count


# Main script
user_input = input("Enter a list of integers (comma-separated): ")
input_list = [int(x) for x in user_input.split(',')]

target_element = int(input("Enter the element to search for: "))

sorted_list = sorted(input_list)

index = binary_search(sorted_list, target_element)

if index == -1:
    print("Element not found in the list.")
else:
    count = count_occurrences(sorted_list, target_element)
    print("Sorted array:", sorted_list)
    print("Number of occurrences of element", target_element, "is:", count)
