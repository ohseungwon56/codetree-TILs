n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

i=a

while i<=b:
    print(i, end=' ')
    if i%2==0:
        i+=3
    else:
        i*=2