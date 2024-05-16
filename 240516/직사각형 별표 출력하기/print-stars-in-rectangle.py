a=input()
arr=a.split()
n=int(arr[0])
m=int(arr[1])
for i in range (1, n+1):
    for j in range (1, m+1):
        print("*", end=' ')
    print(" ")