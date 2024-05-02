def merge(arr,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    for i in range(0, n1):
        L[i] = arr[p+i]
    for j in range(0, n2):
        R[j] = arr[q+j+1]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1



def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

# Take input from the user for the array
arr = input("Enter the elements of the array separated by spaces: ").split()
unsorted_arr = arr.copy()
# Convert input elements to integers
unsorted_arr = [int(x) for x in unsorted_arr]
arr = [int(x) for x in arr]

# Call selection_sort function to sort the array
merge_sort(arr,0,len(arr)-1)

# Print the sorted array
print(len(arr))
print("UnSorted array:", unsorted_arr)
print("Sorted array:", arr)
