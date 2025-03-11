def leap_check(year):
    return (year%400==0)or(year%100!=0 and year%4==0)

month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

while True:
    day, month, year = map(int, input().split())
    if day==month==year==0:
        break

    if not (1<=month<=12):
        print('Invalid')
        continue

    max_days = month_days[month]
    if month==2 and leap_check(year):
        max_days = 29

    if 1<=day<=max_days:
        print('Valid')
    else:
        print('Invalid')