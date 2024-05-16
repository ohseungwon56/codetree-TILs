n=int(input())
cnt=n

for i in range(1, 2*n):
    for j in range(cnt):
        print("*", end=' ')
    print(" ")

    if i<n:
        cnt-=1
    else:
        cnt+=1