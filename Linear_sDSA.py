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
