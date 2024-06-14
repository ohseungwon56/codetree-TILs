k = input()
arr = k.split(sep=' ')
c, n = arr[0], int(arr[1])

if c == 'A':
    for i in range (1, n+1):
        print(i, end=' ')

if c == 'D':
    for j in range(n+1, 1, -1):
        print(j, end=' ')