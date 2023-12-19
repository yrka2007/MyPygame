x1, y1, r1 = input().split()
x1, y1, r1 = int(x1), int(y1), int(r1)
x2, y2, r2 = input().split()
x2, y2, r2 = int(x2), int(y2), int(r2)
a = abs(x1 - x2) ** 2
b = abs(y1 - y2) ** 2
c = (a + b) ** 0.5
if c > r1 + r2:
    print('NO')
else:
    print('YES')


