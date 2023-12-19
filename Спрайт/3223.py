x1, y1, w1, h1 = input().split()
x1, y1, w1, h1 = int(x1), int(y1), int(w1), int(h1)
x2, y2, w2, h2 = input().split()
x2, y2, w2, h2 = int(x2), int(y2), int(w2), int(h2)
if x2 < x1:
    x1, x2 = x2, x1
    w1, w2 = w2, w1
if y2 < y1:
    y1, y2 = y2, y1
    h1, h2 = h2, h1
if x2 - x1 <= w1 and y2 - y1 <= h1:
    print('YES')
else:
    print('NO')
