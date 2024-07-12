x, y = 0, 0
dir_num = 3

dir = input()
for i in range (100000):
    a=list(dir)
    if a[i] == 'L':
        new_dir = (dir_num+3)%4
        dir_num = new_dir
    elif a[i] == 'R':
        new_dir = (dir_num+1)%4
        dir_num = new_dir
    else:
        if dir_num == 0:
            print(x+1, y)
            break
        elif dir_num == 1:
            print(x, y-1)
            break
        elif dir_num == 2:
            print(x-1, y)
            break
        elif dir_num == 3:
            print(x, y+1)
            break