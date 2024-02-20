def selection_sort(arr):
   for i in range(0, len(arr) - 1):
       print(arr)  # Process
       cur_min_idx = i
       for j in range(i + 1, len(arr)):
           if arr[j] <arr[cur_min_idx]:
               cur_min_idx = j

       arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]


arr = [11, 6, 5, 9, 3, 4] #Input: Unsorted Array
selection_sort(arr)
print(arr) #Output: Sorted Array

#By Tazrian Abdus Salam ID:6238024