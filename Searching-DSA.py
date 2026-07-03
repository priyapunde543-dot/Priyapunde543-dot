#unsorted list
#problem 1 Linear search
a = [10, 24, 56, 40, 30]
value = 30

for i in range(len(a)):
    if a[i] == value:
        print("Element found ", i)
        break
else:
    print("Element not found")
#problem 2 
# sorted list
a = [100, 200 ,300, 400, 500]
value = 100
for i in range(len(a)):
    if a[i] == value:
        print("Element found ", i)
        break
else:
    print("Element not found")
#Binary search
def binary(a, v):
    left = 0
    right = len(a) - 1
    while left <= right:
        m = (left + right) // 2
        if a[m] == v:
            return m
        elif a[m] < v:
            left = m + 1
        else:
            right = m - 1
    return -1
a = [2, 4, 6, 8, 10, 12, 14]
v= 10
r = binary(a, v)
if r != -1:
    print("Element found in index:", r)
else:
    print("Element not found")
