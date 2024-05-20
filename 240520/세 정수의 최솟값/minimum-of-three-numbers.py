n=input()
arr=n.split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

sep=0

if a<=b and a<=c:
    sep=a
if b<=a and b<=c:
    sep=b
if c<=a and c<=b:
    sep=c

print(sep)