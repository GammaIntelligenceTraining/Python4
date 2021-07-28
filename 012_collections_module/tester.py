from collections import deque

d = deque()
d.append(1)
d.append(2)
d.extendleft([3, 4, 5])
print(d)
d.rotate(-2)
print(d)