N = int(input())

arr=[]
for i in range(N):
    arr.append(int(input()))

for j in range(N):
    if (arr[j]%2==1 and arr[j]%3==0):
        print(arr[j])