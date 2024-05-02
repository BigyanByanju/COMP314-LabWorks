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

    return arr
