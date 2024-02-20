def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(arr)  # Process
        while arr[i - 1] > arr[i] and i > 0:
            print(arr)
            arr[i - 1], arr[i] = arr[i], arr[i -1]
            i -= 1


arr = [2, 6, 5, 1, 3, 4] #Input: Unsorted Array
insertion_sort(arr)
print(arr) #Output: Sorted Array

#By Chonnseht Phosawatmanee ID:6335405