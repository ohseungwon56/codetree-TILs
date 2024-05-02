n=input()
n=int (n)

for i in range (1000):
    print(n+i, end=' ')
    if(n+i >= 100):
        break;