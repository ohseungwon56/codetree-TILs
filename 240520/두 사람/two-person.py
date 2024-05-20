n=input()
m=input()
a=n.split()
b=m.split()
a_age, a_gender = int(a[0]), a[1]
b_age, b_gender = int(b[0]), b[1]

if (a_age >= 19 or b_age >= 19) and (a_gender=='M' or b_gender=='M'):
    print(1)
else:
    print(0)