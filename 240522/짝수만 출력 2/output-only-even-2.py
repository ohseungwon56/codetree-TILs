n=input()
arr=n.split()
a, b = int(arr[1]), int(arr[0])

n=b
while n>=a:
    print(n)
    n-=2