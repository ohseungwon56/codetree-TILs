x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
N = int(input())
for i in range(N):
    a = input()
    arr = a.split()
    dir = arr[0]
    deg = int(arr[1])

    if dir == "N":
        nx, ny = x+(deg*dx[3]), y+(deg*dy[3])
    if dir == "E":
        nx, ny = x+(deg*dx[0]), y+(deg*dy[0])
    if dir == "S":
        nx, ny = x+(deg*dx[1]), y+(deg*dy[1])
    if dir == "W":
        nx, ny = x+(deg*dx[2]), y+(deg*dy[2])
    x, y = nx, ny

print(x, y)