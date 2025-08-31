month = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0,
         7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}

for _ in range(int(input())):
    E, B = input().split()
    d, m, y = map(int, B.split('/'))
    month[m] += 1

for i in range(1, 13):
    print(i, month[i])