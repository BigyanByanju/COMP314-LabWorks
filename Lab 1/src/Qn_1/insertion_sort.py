# insertion sort

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        # insert arr[j] into the sorted sequence arr[1..j-1]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key


# Take input from the user for the array
arr = input("Enter the elements of the array separated by spaces: ").split()
unsorted_arr = arr.copy()
# Convert input elements to integers
unsorted_arr = [int(x) for x in unsorted_arr]
arr = [int(x) for x in arr]

# Call insertion_sort function to sort the array
insertion_sort(arr)

# Print the sorted array
print("UnSorted array:", unsorted_arr)
print("Sorted array:", arr)
