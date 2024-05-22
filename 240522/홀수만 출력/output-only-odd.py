n=input()
arr=n.split()
a, b = int(arr[0]), int(arr[1])

for i in range(a, b+1, 2):
    if a%2 == 0:
        print(i+1, end=' ')
    else:
        print(i, end = ' ')