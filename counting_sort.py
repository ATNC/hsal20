def counting_sort(arr):
    max_element = max(arr)

    count = [0] * (max_element + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_arr = [0] * len(arr)

    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr


arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
