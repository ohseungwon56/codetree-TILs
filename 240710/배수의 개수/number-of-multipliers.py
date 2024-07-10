cnt_five, cnt_three = 0, 0
for i in range(10):
    a = int(input())
    if (a%3==0):
        cnt_three+=1
    if (a%5==0):
        cnt_five+=1

print(cnt_three, cnt_five)