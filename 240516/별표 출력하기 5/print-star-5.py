n=int(input())
for i in range (1, n+1):
    for j in range(n+1-i, 0, -1):
        for k in range(n+1-i, 0, -1):
            print("*", end='')
        print(" ", end='')
    print(" ")