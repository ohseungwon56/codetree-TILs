n=int(input())
for i in range(1, n+1):
    if i%3 == 0:
        print(0, end=' ')
    elif i%3 == 1:
        print(1, end=' ')
    else:
        print(2, end=' ')