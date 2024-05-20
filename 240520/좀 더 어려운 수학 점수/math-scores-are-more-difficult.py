n=input()
m=input()
a, b = n.split(), m.split()
a_math, a_eng = int(a[0]), int(a[1])
b_math, b_eng = int(b[0]), int(b[1])

if a_math > b_math:
    print("A")
elif a_math < b_math:
    print("B")
if (a_math == b_math) and (a_eng > b_eng):
    print("A")
elif (a_math == b_math) and (a_eng < b_eng):
    print("B")