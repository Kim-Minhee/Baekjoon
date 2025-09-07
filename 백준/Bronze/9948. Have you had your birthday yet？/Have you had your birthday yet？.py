import calendar

month = list(calendar.month_name)
while True:
    B = input()
    if B == '0 #':
        break
    
    d, m = B.split()
    if m == 'February' and d == '29':
        print('Unlucky')
    elif m == 'August' and d == '4':
        print('Happy birthday')
    elif month.index(m) < 8 or (month.index(m) == 8 and int(d) < 4):
        print('Yes')
    else:
        print('No')