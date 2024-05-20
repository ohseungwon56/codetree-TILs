n=input()
m=input()
arr1=n.split()
arr2=m.split()
a_math=int(arr1[0])
a_eng=int(arr1[1])
b_math=int(arr2[0])
b_eng=int(arr2[1])

if (a_math > b_math) and (a_eng > b_eng):
    print(1)
else:
    print(0)