a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
list=[a, b, c]
d= sum(list) / len(list)
d=int(d)
print(sum(list))
print(d)
print(sum(list)-d)