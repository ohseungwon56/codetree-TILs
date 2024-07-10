n = int(input())
cnt_two, cnt_three, cnt_twel = 0, 0, 0
for i in range(1, n+1):
    if (i%12==0):
        cnt_twel += 1
    elif (i%3==0):
        cnt_three += 1
    elif (i%2==0):
        cnt_two += 1
print(cnt_two, cnt_three, cnt_twel)