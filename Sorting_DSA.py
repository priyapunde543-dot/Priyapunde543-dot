#Bubble sorting
array = [7, 4, 2, 34]
n = len(array)
for i in range(n):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("Sorted Array:", array)
#Selection sort
arr = [1, 2, 39, 14, 19]
for i in range(len(arr)):
    m_i = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[m_i]:
            m_i= j
    arr[i], arr[m_i] = arr[m_i], arr[i]
print(arr)
#Insertion sort
arr = [5, 3, 8, 4, 2]

for i in range(1, len(arr)):
    value = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > value:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = value
print(arr)
#Quick sort
def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick(left) + [pivot] + quick(right)

arr = [5, 3, 8, 4, 2]
print(quick(arr))
#Merge sort
def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        arr[:] = sorted(left + right)
arr = [5, 3, 8, 4, 2]
merge(arr)
print(arr)
