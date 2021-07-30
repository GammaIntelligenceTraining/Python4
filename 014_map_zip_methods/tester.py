import random

data1 = [100, 200, 300, 400, 500, 600, 700]
data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

empty_list = []
cnt = 0
while cnt < 7:
    empty_list.append(random.randrange(1, 100) / 10)
    cnt += 1
zipped_list = zip(data2, empty_list)


for a, b in zipped_list:
    print(a)
    print(b)

