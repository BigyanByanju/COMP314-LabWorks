# Selection Sort

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        temp = arr[i]
        arr[i] = arr[m]
        arr[m] = temp


# Take input from the user for the array
arr = input("Enter the elements of the array separated by spaces: ").split()
unsorted_arr = arr.copy()
# Convert input elements to integers
unsorted_arr = [int(x) for x in unsorted_arr]
arr = [int(x) for x in arr]

# Call selection_sort function to sort the array
selection_sort(arr)

# Print the sorted array
print(len(arr))
print("UnSorted array:", unsorted_arr)
print("Sorted array:", arr)
