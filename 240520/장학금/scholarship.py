n=input()
arr=n.split()
mid, fin = int(arr[0]), int(arr[1])
if mid >= 90 and (fin >= 95 and fin <=100):
    print(100000)
elif mid >= 90 and fin >= 90:
    print(50000)
else:
    print(0)