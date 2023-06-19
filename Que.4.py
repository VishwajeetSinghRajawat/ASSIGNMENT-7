def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Take input from the user for number of students and their marks
n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    mark = int(input("Enter the mark for student {}: ".format(i + 1)))
    marks.append(mark)

# Sort the list using quicksort
sorted_marks = quick_sort(marks)

# Print the final sorted list
print("List after sorting is:", sorted_marks)
