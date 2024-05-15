n=input()
m=n.split()
a_math=int(m[0])
a_eng=int(m[1])

x=input()
y=x.split()
b_math=int(y[0])
b_eng=int(y[1])

if a_math>b_math and a_eng>b_eng:
    print(1)