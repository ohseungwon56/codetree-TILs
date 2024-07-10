sum=0
cnt=0
a, b = map(int, input().split())
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        sum+=i
        cnt+=1

ave = sum/cnt

print(f'{sum} {ave:.1f}')