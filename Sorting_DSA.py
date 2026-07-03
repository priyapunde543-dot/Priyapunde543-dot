#Bubble sorting
array = [7, 4, 2, 34]
n = len(array)
for i in range(n):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("Sorted Array:", array)
