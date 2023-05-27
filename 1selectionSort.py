def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Accept input from the user
input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(num) for num in input_str.split()]

# Call the selection_sort function and print the result
sorted_list = selection_sort(input_list)
print("Sorted list:", sorted_list)
