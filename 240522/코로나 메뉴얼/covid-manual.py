a=input()
b=input()
c=input()

arr_a=a.split()
arr_b=b.split()
arr_c=c.split()

a_cold, a_temp = arr_a[0], int(arr_a[1])
b_cold, b_temp = arr_b[0], int(arr_b[1])
c_cold, c_temp = arr_c[0], int(arr_c[1])

if a_cold == "Y" and a_temp >= 37:
    a_manual = "A"
elif a_cold == "N" and a_temp >=37:
    a_manual = "B"
elif a_cold == "Y" and a_temp < 37:
    a_manual = "C"
else:
    a_manual = "D"

if b_cold == "Y" and b_temp >= 37:
    b_manual = "A"
elif b_cold == "N" and b_temp >= 37:
    b_manual = "B"
elif b_cold == "Y" and b_temp < 37:
    b_manual = "C"
else:
    b_manual = "D"

if c_cold == "Y" and c_temp >= 37:
    c_manual = "A"
elif c_cold == "N" and c_temp >= 37:
    c_manual = "B"
elif c_cold == "Y" and c_temp < 37:
    c_manual = "C"
else:
    c_manual = "D"

if (a_manual == "A" and b_manual == "A" and c_manual != "A") or (a_manual == "A" and b_manual != "A" and c_manual == "A") or (a_manual != "A" and b_manual == "A" and c_manual == "A") or (a_manual == 'A' and b_manual == "A" and c_manual == "A"):
    print("E")
else:
    print("N")