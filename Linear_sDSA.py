#problem 1 Linear search
a = [10, 24, 56, 40, 30]
value = 30

for i in range(len(a)):
    if a[i] == value:
        print("Element found ", i)
        break
else:
    print("Element not found")
