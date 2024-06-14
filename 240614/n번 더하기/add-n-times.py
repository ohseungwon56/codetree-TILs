n = input()
arr = n.split()
a, n = int(arr[0]), int(arr[1])

for i in range (1, n+1):
    print(a+n*i)