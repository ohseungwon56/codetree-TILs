n=input()
arr=n.split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

if a<=b and a<=c:
    print(1, end=" ")
else:
    print(0, end=" ")

if a==b and b==c and c==a:
    print(1, end=" ")
else:
    print(0, end=" ")